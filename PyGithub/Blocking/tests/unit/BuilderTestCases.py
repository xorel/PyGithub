# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import io
import sys
import unittest

import requests
import MockMockMock

import PyGithub.Blocking._builder as bld


class RequestMatcher(object):
    def __init__(self, verb, url, headers, body):
        self.__verb = verb
        self.__url = url
        self.__headers = headers
        self.__body = body

    def __call__(self, args, kwds):
        request = args[0]
        if self.check(request):
            return True
        else:
            print(request.method, request.url, request.headers, request.body, "instead of", self.__verb, self.__url, self.__headers, self.__body)  # pragma no cover
            return False  # pragma no cover

    def check(self, request):
        return (
            request.method == self.__verb
            and request.url == self.__url
            and dict(request.headers) == self.__headers
            and request.body == self.__body
        )


def rebuildResponse(status, headers, body):
    response = requests.Response()
    response.status_code = status
    response.headers = requests.structures.CaseInsensitiveDict(headers)
    if sys.hexversion >= 0x03000000:
        body = bytes(body, encoding="utf8")  # pragma no cover
    response.raw = requests.packages.urllib3.HTTPResponse(
        io.BytesIO(body),
        status=status,
        headers=headers,
        preload_content=False
    )
    return response


class BuilderTestCase(unittest.TestCase):
    def setUp(self):
        super(BuilderTestCase, self).setUp()
        self.mocks = MockMockMock.Engine()
        self.adapter = self.mocks.create("adapter")

    def tearDown(self):
        super(BuilderTestCase, self).tearDown()
        self.mocks.tearDown()

    def makeSession(self, b):
        s = b.Build().Session
        for k, v in s._Session__requestsSession.adapters.iteritems():
            s._Session__requestsSession.mount(k, self.adapter.object)
        for k, v in s._Session__anonymousRequestsSession.adapters.iteritems():
            s._Session__anonymousRequestsSession.mount(k, self.adapter.object)
        return s

    def testNoArgument(self):
        s = self.makeSession(bld.Builder())
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": bld.Builder.defaultUserAgent}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = s._request("GET", "http://foo.com")
        self.assertEqual(response.status_code, 200)

    def testUserAgent(self):
        s = self.makeSession(bld.Builder().UserAgent("user-agent"))
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = s._request("GET", "http://foo.com")
        self.assertEqual(response.status_code, 200)

    def testPerPage(self):
        s = self.makeSession(bld.Builder().PerPage(42))
        self.assertEqual(s.PerPage, 42)

    def testLogin(self):
        s = self.makeSession(bld.Builder().Login("login", "password"))
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Authorization": "Basic bG9naW46cGFzc3dvcmQ=", "Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": bld.Builder.defaultUserAgent}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = s._request("GET", "http://foo.com")
        self.assertEqual(response.status_code, 200)

    def testOAuth(self):
        s = self.makeSession(bld.Builder().OAuth("token"))
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Authorization": "token token", "Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": bld.Builder.defaultUserAgent}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = s._request("GET", "http://foo.com")
        self.assertEqual(response.status_code, 200)

    def testApplication(self):
        s = self.makeSession(bld.Builder().Application("id", "secret"))
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/?client_secret=secret&client_id=id", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": bld.Builder.defaultUserAgent}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = s._request("GET", "http://foo.com")
        self.assertEqual(response.status_code, 200)

    def testEnterprise(self):
        s = self.makeSession(bld.Builder().Enterprise("net.loc"))
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://net.loc/api/v3/foo", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": bld.Builder.defaultUserAgent}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = s._request("GET", "https://api.github.com/foo")
        self.assertEqual(response.status_code, 200)
