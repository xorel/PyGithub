# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class UnusualErrorsTestCase(TestCase):
    def testInternalError(self):
        with self.assertRaises(PyGithub.Blocking.ServerErrorException) as cm:
            self.dotcom.get_authenticated_user()
        self.assertEqual(
            cm.exception.args,
            (
                502,
                {"date": "Sun, 22 Dec 2013 22:50:19 GMT", "content-length": "32", "content-type": "application/json", "server": "GitHub.com"},
                {"message": "Server Error"}
            )
        )

    def testConsumeRateLimit(self):
        g = self.getBuilder().Build()

        g.get_user("nvie")
        for i in range(g.Session.RateLimit.remaining):
            g.get_user("nvie")
        self.assertEqual(g.Session.RateLimit.remaining, 0)

        with self.assertRaises(PyGithub.Blocking.RateLimitExceededException):
            g.get_user("nvie")
        self.assertEqual(g.Session.RateLimit.remaining, 0)
