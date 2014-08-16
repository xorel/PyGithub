# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class UnauthenticatedTestCase(TestCase):
    def testGetAuthenticatedUser(self):
        g = self.getBuilder().Build()
        with self.assertRaises(PyGithub.Blocking.UnauthorizedException):
            g.get_authenticated_user()

# @todoAlpha When PyGithub implements authorizations, use it to create tokens to test OAuth
# class OAuthWithoutScopesTestCase(Framework.SimpleOAuthWithoutScopesTestCase):
#     def testGetAuthenticatedUser(self):
#         self.assertEqual("jacquev6", self.g.get_authenticated_user().login)
#         self.assertEqual(self.g.Session.OAuthScopes, [])
#         self.assertEqual(self.g.Session.AcceptedOAuthScopes, [])

#     def testModifySomething(self):
#         with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException) as cm:
#             self.g.get_authenticated_user().edit(location="The Moon")
#         self.assertEqual(self.g.Session.OAuthScopes, [])


# class OAuthWithScopesTestCase(Framework.SimpleOAuthWithScopesTestCase):
#     def testEditAuthentic(self):
#         self.g.get_authenticated_user().edit(location="The Moon")
#         self.assertEqual(self.g.Session.OAuthScopes, ["repo", "user"])
#         self.assertEqual(self.g.Session.AcceptedOAuthScopes, ["user"])
