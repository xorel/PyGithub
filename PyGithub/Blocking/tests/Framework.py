# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import datetime
import inspect
import io
import json
import logging
import os.path
import sys
import time
import unittest
import urlparse
import zlib

import requests
import MockMockMock

import PyGithub


try:
    import GithubCredentials
    DotComLogin = GithubCredentials.login
    DotComPassword = GithubCredentials.password
except ImportError:
    DotComLogin = "login"
    DotComPassword = "password"


class _RecordModeHelper(object):
    @staticmethod
    def sanitize(request):
        if "Authorization" in request.headers and request.headers["Authorization"] not in [
            "Basic emV1czpwYXNzd29yZDEtemV1cw==",  # Zeus
            "Basic cG9zZWlkb246cGFzc3dvcmQxLXBvc2VpZG9u",  # Poseidon
            "Basic YW50aWdvbmU6cGFzc3dvcmQxLWFudGlnb25l",  # Antigone
            "Basic cGVuZWxvcGU6cGFzc3dvcmQxLXBlbmVsb3Bl",  # Penelope
            "Basic ZWxlY3RyYTpwYXNzd29yZDEtZWxlY3RyYQ==",  # Electra

            "token 05609fccd5491c0dc684e2577572794dd3c1a642",  # AuthenticationTestCases.py OAuthTestCase

            "Basic Z2hlLXVzZXItMTpwYXNzd29yZC11c2VyLTE=",  # ghe-user-1, temporary
            "Basic Z2hlLXVzZXItMjpwYXNzd29yZC11c2VyLTI=",  # ghe-user-2, temporary
        ]:
            assert request.headers["Authorization"].startswith("Basic "), request.headers["Authorization"]
            request.headers["Authorization"] = "Basic removed="

    @staticmethod
    def parseUrl(url):
        parse = urlparse.urlparse(url)
        return {
            "scheme": parse.scheme,
            "netloc": parse.netloc,
            "path": parse.path,
            "query": dict(urlparse.parse_qsl(parse.query)),
        }

    class RecordMode(object):
        def __init__(self, instance, fileName):
            logging.getLogger("PyGithub").setLevel(logging.DEBUG)
            self.__instance = instance
            self.__fileName = fileName

        def apply(self, g):
            s = g.Session
            for k, v in s._Session__requestsSession.adapters.iteritems():
                s._Session__requestsSession.mount(k, self.__instance.adapter.record(v))
            for k, v in s._Session__anonymousRequestsSession.adapters.iteritems():
                s._Session__anonymousRequestsSession.mount(k, self.__instance.adapter.record(v))

        def pause(self, duration):
            time.sleep(duration)

        def finalize(self):
            interractions = []
            for record in self.__instance.mocks.records:
                response = record["return"]
                request = response.request
                _RecordModeHelper.sanitize(request)
                try:
                    requestBody = json.loads(request.body)
                    requestIsJson = True
                except:
                    requestBody = request.body
                    requestIsJson = False
                try:
                    responseBody = json.loads(response.content)
                    responseIsJson = True
                except:
                    responseBody = response.content
                    responseIsJson = False
                interractions.append({
                    "request": {
                        'body': requestBody,
                        'headers': dict(request.headers),
                        'verb': request.method,
                        'url': _RecordModeHelper.parseUrl(request.url),
                        'is_json': requestIsJson,
                    },
                    "response": {
                        'body': responseBody,
                        'headers': dict(response.headers),
                        'status': response.status_code,
                        'is_json': responseIsJson,
                    },
                })
            if not os.path.exists(os.path.dirname(self.__fileName)):
                os.makedirs(os.path.dirname(self.__fileName))
            with open(self.__fileName, "w") as f:
                json.dump(interractions, f, sort_keys=True, indent=4, separators=(',', ': '))

    class ReplayMode(object):
        class RequestMatcher(object):
            def __init__(self, verb, url, headers, body, is_json):
                self.__verb = verb
                self.__url = url
                self.__headers = headers
                self.__body = body
                self.__isJson = is_json

            def __call__(self, args, kwds):
                request = args[0]
                _RecordModeHelper.sanitize(request)
                if self.check(request):
                    return True
                else:
                    print(request.url, request.headers, "instead of", self.__url, self.__headers)
                    return False

            def check(self, request):
                if self.__isJson:
                    requestBody = json.loads(request.body)
                else:
                    requestBody = request.body
                return (
                    request.method == self.__verb
                    and _RecordModeHelper.parseUrl(request.url) == self.__url
                    and request.headers == self.__headers
                    and requestBody == self.__body
                )

        def __init__(self, instance, fileName):
            logging.getLogger("PyGithub").setLevel(logging.INFO)
            self.__instance = instance
            self.__fileName = fileName
            with open(self.__fileName) as f:
                records = json.load(f)
            for record in records:
                self.__instance.adapter.expect.send.withArguments(
                    self.RequestMatcher(**record["request"])
                ).andReturn(
                    self.__rebuildResponse(**record["response"])
                )

        def __rebuildResponse(self, status, headers, body, is_json):
            response = requests.Response()
            response.status_code = status
            response.headers = requests.structures.CaseInsensitiveDict(headers)

            if is_json:
                body = json.dumps(body)
            body = body.encode("utf8")

            if "content-encoding" in headers:
                assert headers["content-encoding"] == "gzip"
                c = zlib.compressobj(6, zlib.DEFLATED, 16 + zlib.MAX_WBITS)
                body = c.compress(body) + c.flush()

            response.raw = requests.packages.urllib3.HTTPResponse(
                io.BytesIO(body),
                status=status,
                headers=headers,
                preload_content=False
            )
            return response

        def apply(self, g):
            s = g.Session
            for k, v in s._Session__requestsSession.adapters.iteritems():
                s._Session__requestsSession.mount(k, self.__instance.adapter.object)
            for k, v in s._Session__anonymousRequestsSession.adapters.iteritems():
                s._Session__anonymousRequestsSession.mount(k, self.__instance.adapter.object)

        def pause(self, duration):
            pass

        def finalize(self):
            pass

    def __init__(self, instance, methodName):
        assert isinstance(instance, TestCase)
        pythonFileName = inspect.getfile(instance.__class__)
        fileName = "{}/{}_RecordedData/{}.{}.json".format(os.path.dirname(pythonFileName), os.path.splitext(os.path.basename(pythonFileName))[0], instance.__class__.__name__, methodName)
        if os.path.exists(fileName):
            self.__mode = self.ReplayMode(instance, fileName)
        else:
            self.__mode = self.RecordMode(instance, fileName)

    def apply(self, g):
        self.__mode.apply(g)

    def pause(self, duration):
        self.__mode.pause(duration)

    def finalize(self):
        self.__mode.finalize()


class TestCase(unittest.TestCase):
    data = None

    def pause(self, duration=5):
        if hasattr(self, "_TestCase__recordHelper"):
            self.__recordHelper.pause(duration)
        else:
            time.sleep(duration)

    def setUpTestRepo(self, owner, name, **kwds):
        g = getattr(self, owner)
        try:
            g.get_repo((owner, name)).delete()
            self.pause()
        except PyGithub.Blocking.ObjectNotFoundException:
            pass
        if "auto_init" not in kwds:
            kwds["auto_init"] = True
        repo = g.get_authenticated_user().create_repo(name, **kwds)
        self.pause()
        return repo

    def getBuilder(self):
        builder = PyGithub.BlockingBuilder().UserAgent("jacquev6/PyGithub/2; UnitTests recorder")
        if hasattr(self, "_TestCase__recordHelper"):
            origBuild = builder.Build

            def newBuild(*args, **kwds):
                github = origBuild(*args, **kwds)
                self.__recordHelper.apply(github)
                return github

            builder.Build = newBuild
        return builder

    def getEnterpriseBuilder(self):
        return self.getBuilder().Enterprise("github.home.jacquev6.net")

    def setUp(self):
        super(TestCase, self).setUp()
        self.__setUpResourcesIfNeeded()
        self.__setUpMocks(self._testMethodName)

    def __setUpResourcesIfNeeded(self):
        if self.__class__.data is None and hasattr(self, "setUpEnterprise"):
            self.__setUpResources()

    def __setUpResources(self):
        pythonFileName = inspect.getfile(self.__class__)
        fileName = "{}/{}_RecordedData/{}.setUpEnterprise.json".format(os.path.dirname(pythonFileName), os.path.splitext(os.path.basename(pythonFileName))[0], self.__class__.__name__)
        if os.path.exists(fileName):
            with open(fileName) as f:
                self.__class__.data = Data(**json.load(f))
        else:
            self.__class__.data = object()
            self.__setUpUsers()
            logging.getLogger("PyGithub").setLevel(logging.DEBUG)
            self.__class__.data = self.setUpEnterprise()
            logging.getLogger("PyGithub").setLevel(logging.INFO)
            assert isinstance(self.__class__.data, Data)
            if not os.path.exists(os.path.dirname(fileName)):
                os.makedirs(os.path.dirname(fileName))
            with open(fileName, "w") as f:
                json.dump(self.__class__.data._raw, f, sort_keys=True, indent=4, separators=(',', ': '))

    def __setUpMocks(self, methodName):
        self.mocks = MockMockMock.Engine()
        self.adapter = self.mocks.create("adapter")
        self.__recordHelper = _RecordModeHelper(self, methodName)
        self.__setUpUsers()

    def __setUpUsers(self):
        self.dotcom = self.getBuilder().Login(DotComLogin, DotComPassword).Build()
        self.dotcom4 = self.getBuilder().Login(DotComLogin, DotComPassword).PerPage(4).Build()  # @todoAlpha Remove all tests using dotcom4
        for login in ["zeus", "poseidon", "antigone", "electra", "penelope", "morpheus"]:
            password = "password1-{}".format(login)
            github = self.getBuilder().Enterprise("github.home.jacquev6.net").Login(login, password).Build()
            setattr(self, login, github)
        for i in [1, 2]:  # @todoAlpha Remove all tests using ghe-user-1 or ghe-user-1
            name = "user{}".format(i)
            login = "ghe-user-{}".format(i)
            password = "password-user-{}".format(i)
            github = self.getBuilder().Enterprise("github.home.jacquev6.net").Login(login, password).Build()
            setattr(self, name, github)

    def tearDown(self):
        super(TestCase, self).tearDown()
        self.__recordHelper.finalize()
        self.mocks.tearDown()


class Data(object):
    def __init__(self, **kwds):
        self._raw = dict(kwds)
        for k, v in self._raw.iteritems():
            assert not k.startswith("_")
            setattr(self, k, v)
