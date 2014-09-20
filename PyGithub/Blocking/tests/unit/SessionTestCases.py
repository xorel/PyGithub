# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import datetime
import io
import logging
import sys
import unittest

import requests
import MockMockMock

import PyGithub.Blocking
import PyGithub.Blocking._session as ses

import PyGithub.Blocking.tests.Framework as Framework


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
            and Framework._RecordModeHelper.parseUrl(request.url) == Framework._RecordModeHelper.parseUrl(self.__url)
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


class SessionTestCase(unittest.TestCase):
    def setUp(self):
        super(SessionTestCase, self).setUp()
        self.mocks = MockMockMock.Engine()
        self.adapter = self.mocks.create("adapter")

    def tearDown(self):
        super(SessionTestCase, self).tearDown()
        self.mocks.tearDown()

    def makeSession(self, *args, **kwds):
        s = ses.Session(*args, **kwds)
        for k, v in s._Session__requestsSession.adapters.iteritems():
            s._Session__requestsSession.mount(k, self.adapter.object)
        for k, v in s._Session__anonymousRequestsSession.adapters.iteritems():
            s._Session__anonymousRequestsSession.mount(k, self.adapter.object)
        return s


class RequestsTestCase(SessionTestCase):
    def setUp(self):
        super(RequestsTestCase, self).setUp()
        self.session = self.makeSession(ses._AnonymousAuthenticator(), None, None, "user-agent")

    def testSimplestRequest(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = self.session._request("GET", "http://foo.com")
        self.assertEqual(response.status_code, 200)

    def testRequestWithEverything(self):
        self.adapter.expect.send.withArguments(RequestMatcher("POST", "http://foo.com/bar/baz?urlArgument=query-value", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent", "header": "header-value", "Content-Length": "30"}, '{"postArgument": "post-value"}')).andReturn(rebuildResponse(200, dict(), ""))
        response = self.session._request("POST", "http://foo.com/bar/baz", urlArguments=dict(urlArgument="query-value"), postArguments=dict(postArgument="post-value"), headers=dict(header="header-value"))
        self.assertEqual(response.status_code, 200)

    def testRequestWithPayloadAlreadyEncoded(self):
        self.adapter.expect.send.withArguments(RequestMatcher("POST", "http://foo.com/", {"Content-Type": "text/plain", "Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent", "Content-Length": "12"}, 'post-payload')).andReturn(rebuildResponse(200, dict(), ""))
        response = self.session._request("POST", "http://foo.com", postArguments="post-payload", headers={"Content-Type": "text/plain"})
        self.assertEqual(response.status_code, 200)

    def testRequestWithTrueBooleanUrlArgument(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/?t=true", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = self.session._request("GET", "http://foo.com", urlArguments=dict(t=True))
        self.assertEqual(response.status_code, 200)

    def testRequestWithFalseBooleanUrlArgument(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/?f=false", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = self.session._request("GET", "http://foo.com", urlArguments=dict(f=False))
        self.assertEqual(response.status_code, 200)

    def testUpdateRateLimit(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, {"x-ratelimit-limit": "42", "x-ratelimit-remaining": "57", "x-ratelimit-reset": "1408161103"}, ""))
        self.session._request("GET", "http://foo.com")
        self.assertEqual(self.session.RateLimit.limit, 42)
        self.assertEqual(self.session.RateLimit.remaining, 57)
        self.assertEqual(self.session.RateLimit.reset, datetime.datetime(2014, 8, 16, 3, 51, 43))

    def testGetInitialRateLimit(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "https://api.github.com/rate_limit", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, {"x-ratelimit-limit": "42", "x-ratelimit-remaining": "57", "x-ratelimit-reset": "1408161103"}, ""))
        self.assertEqual(self.session.RateLimit.limit, 42)
        self.assertEqual(self.session.RateLimit.remaining, 57)
        self.assertEqual(self.session.RateLimit.reset, datetime.datetime(2014, 8, 16, 3, 51, 43))

    def testUpdateOAuthScopes(self):
        self.assertEqual(self.session.AcceptedOAuthScopes, None)
        self.assertEqual(self.session.OAuthScopes, None)
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, {"x-oauth-scopes": "a, b", "x-accepted-oauth-scopes": "b, c, d"}, ""))
        self.session._request("GET", "http://foo.com")
        self.assertEqual(self.session.AcceptedOAuthScopes, ["b", "c", "d"])
        self.assertEqual(self.session.OAuthScopes, ["a", "b"])
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, {"x-oauth-scopes": "", "x-accepted-oauth-scopes": ""}, ""))
        self.session._request("GET", "http://foo.com")
        self.assertEqual(self.session.AcceptedOAuthScopes, [])
        self.assertEqual(self.session.OAuthScopes, [])
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, {}, ""))
        self.session._request("GET", "http://foo.com")
        self.assertEqual(self.session.AcceptedOAuthScopes, None)
        self.assertEqual(self.session.OAuthScopes, None)


class AuthentifiedRequests(SessionTestCase):
    def setUp(self):
        super(AuthentifiedRequests, self).setUp()
        self.session = self.makeSession(ses._LoginAuthenticator("login", "password"), None, None, "user-agent")

    def testAuthentifiedRequest(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Authorization": "Basic bG9naW46cGFzc3dvcmQ=", "Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = self.session._request("GET", "http://foo.com")
        self.assertEqual(response.status_code, 200)

    def testAnonymousRequest(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = self.session._requestAnonymous("GET", "http://foo.com")
        self.assertEqual(response.status_code, 200)


class CustomNetlocRequests(SessionTestCase):
    def test(self):
        s = self.makeSession(ses._AnonymousAuthenticator(), "net.loc", None, "user-agent")
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://net.loc/api/v3/foo", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(), ""))
        response = s._request("GET", "https://api.github.com/foo")
        self.assertEqual(response.status_code, 200)


class CustomPerPage(SessionTestCase):
    def test(self):
        s = self.makeSession(ses._AnonymousAuthenticator(), None, 42, "user-agent")
        self.assertEqual(s.PerPage, 42)


class ExceptionsTestCase(SessionTestCase):
    def setUp(self):
        super(ExceptionsTestCase, self).setUp()
        self.session = self.makeSession(ses._AnonymousAuthenticator(), None, None, "user-agent")

    def test4XX(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "https://api.github.com/rate_limit", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, {"x-ratelimit-limit": "42", "x-ratelimit-remaining": "57", "x-ratelimit-reset": "1408161103"}, ""))
        self.assertEqual(self.session.RateLimit.limit, 42)
        for i in range(400, 500):
            self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(i, dict(), "{}"))
            with self.assertRaises(PyGithub.Blocking.ClientErrorException):
                self.session._request("GET", "http://foo.com")

    def test401(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(401, dict(), "{}"))
        with self.assertRaises(PyGithub.Blocking.UnauthorizedException):
            self.session._request("GET", "http://foo.com")

    def test401WithOtp(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(401, {"X-GitHub-OTP": "required; app"}, "{}"))
        with self.assertRaises(PyGithub.Blocking.OtpRequiredException):
            self.session._request("GET", "http://foo.com")

    def test403WithRateLimitRemaining(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(403, {"x-ratelimit-limit": "42", "x-ratelimit-remaining": "1", "x-ratelimit-reset": "1408161103"}, "{}"))
        with self.assertRaises(PyGithub.Blocking.ForbiddenException):
            self.session._request("GET", "http://foo.com")

    def test403WithRateLimitExceeded(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(403, {"x-ratelimit-limit": "42", "x-ratelimit-remaining": "0", "x-ratelimit-reset": "1408161103"}, "{}"))
        with self.assertRaises(PyGithub.Blocking.RateLimitExceededException):
            self.session._request("GET", "http://foo.com")

    def test404Accepted(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(404, dict(), "{}"))
        response = self.session._request("GET", "http://foo.com", accept404=True)
        self.assertEqual(response.status_code, 404)

    def test404(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(404, dict(), "{}"))
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            self.session._request("GET", "http://foo.com")

    def test405(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(405, dict(), "{}"))
        with self.assertRaises(PyGithub.Blocking.MethodNotAllowedException):
            self.session._request("GET", "http://foo.com")

    def test409(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(409, dict(), "{}"))
        with self.assertRaises(PyGithub.Blocking.ConflictException):
            self.session._request("GET", "http://foo.com")

    def test422(self):
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(422, dict(), "{}"))
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            self.session._request("GET", "http://foo.com")

    def test5XX(self):
        for i in range(500, 600):
            self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://foo.com/", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(i, dict(), "{}"))
            with self.assertRaises(PyGithub.Blocking.ServerErrorException):
                self.session._request("GET", "http://foo.com")


class LoggingTestCase(SessionTestCase):
    def setUp(self):
        super(LoggingTestCase, self).setUp()
        self.log = self.mocks.replace("ses.log")

    def testLogDisabled(self):
        s = self.makeSession(ses._AnonymousAuthenticator(), "net.loc", None, "user-agent")
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://net.loc/api/v3/foo", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(), ""))
        self.log.expect.isEnabledFor(logging.DEBUG).andReturn(False)
        response = s._request("GET", "https://api.github.com/foo")
        self.assertEqual(response.status_code, 200)

    def testLogWithoutAuthentication(self):
        s = self.makeSession(ses._AnonymousAuthenticator(), "net.loc", None, "user-agent")
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://net.loc/api/v3/foo", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(header="value"), "response"))
        self.log.expect.isEnabledFor(logging.DEBUG).andReturn(True)
        self.log.expect.debug("GET http://net.loc/api/v3/foo [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('User-Agent', 'user-agent')] None => 200 [('header', 'value')] response")
        response = s._request("GET", "https://api.github.com/foo")
        self.assertEqual(response.status_code, 200)

    def testLogWithBasicAuthentication(self):
        s = self.makeSession(ses._LoginAuthenticator("login", "password"), "net.loc", None, "user-agent")
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://net.loc/api/v3/foo", {"Authorization": "Basic bG9naW46cGFzc3dvcmQ=", "Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(header="value"), "response"))
        self.log.expect.isEnabledFor(logging.DEBUG).andReturn(True)
        self.log.expect.debug("GET http://net.loc/api/v3/foo [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('Authorization', 'Basic not_logged'), ('User-Agent', 'user-agent')] None => 200 [('header', 'value')] response")
        response = s._request("GET", "https://api.github.com/foo")
        self.assertEqual(response.status_code, 200)

    def testLogWithOauthAuthentication(self):
        s = self.makeSession(ses._OauthAuthenticator("token"), "net.loc", None, "user-agent")
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://net.loc/api/v3/foo", {"Authorization": "token token", "Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(header="value"), "response"))
        self.log.expect.isEnabledFor(logging.DEBUG).andReturn(True)
        self.log.expect.debug("GET http://net.loc/api/v3/foo [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('Authorization', 'token not_logged'), ('User-Agent', 'user-agent')] None => 200 [('header', 'value')] response")
        response = s._request("GET", "https://api.github.com/foo")
        self.assertEqual(response.status_code, 200)

    def testLogWithApplicationAuthentication(self):
        s = self.makeSession(ses._ApplicationAuthenticator("id", "secret"), "net.loc", None, "user-agent")
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://net.loc/api/v3/foo?client_secret=secret&client_id=id", {"Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(header="value"), "response"))
        self.log.expect.isEnabledFor(logging.DEBUG).andReturn(True)
        self.log.expect.debug("GET http://net.loc/api/v3/foo?client_id=id&client_secret=not_logged [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('User-Agent', 'user-agent')] None => 200 [('header', 'value')] response")
        response = s._request("GET", "https://api.github.com/foo")
        self.assertEqual(response.status_code, 200)

    def testLogWithUnknownAuthentication(self):
        class Authenticator(object):
            def prepareSession(self, session):
                session.headers["Authorization"] = "how strange!"
        s = self.makeSession(Authenticator(), "net.loc", None, "user-agent")
        self.adapter.expect.send.withArguments(RequestMatcher("GET", "http://net.loc/api/v3/foo", {"Authorization": "how strange!", "Accept-Encoding": "gzip, deflate, compress", "Accept": "application/vnd.github.v3.full+json", "User-Agent": "user-agent"}, None)).andReturn(rebuildResponse(200, dict(header="value"), "response"))
        self.log.expect.isEnabledFor(logging.DEBUG).andReturn(True)
        self.log.expect.debug("GET http://net.loc/api/v3/foo [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('Authorization', 'Unknown not_logged'), ('User-Agent', 'user-agent')] None => 200 [('header', 'value')] response")
        response = s._request("GET", "https://api.github.com/foo")
        self.assertEqual(response.status_code, 200)
