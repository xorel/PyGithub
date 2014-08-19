# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *

# @todoAlpha What about 2 factors authentication?


class UnauthenticatedTestCase(TestCase):
    def testGetAuthenticatedUser(self):
        g = self.getEnterpriseBuilder().Build()
        with self.assertRaises(PyGithub.Blocking.UnauthorizedException):
            g.get_authenticated_user()


class OAuthTestCase(TestCase):
    def setUpEnterprise(self):
        user = self.electra.get_authenticated_user()
        for a in user.get_authorizations():
            if a.note == "no-scope":
                a.delete()
        a = user.create_authorization("no-scope")
        return Data(id=a.id, token=a.token)

    def testGetAuthenticatedUser(self):
        g = self.getEnterpriseBuilder().OAuth(self.data.token).Build()
        self.assertEqual(g.get_authenticated_user().login, "electra")
        self.assertEqual(g.Session.OAuthScopes, [])
        self.assertEqual(g.Session.AcceptedOAuthScopes, [])

    def testModifySomething(self):
        g = self.getEnterpriseBuilder().OAuth(self.data.token).Build()
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            g.get_authenticated_user().edit(location="The Moon")
        self.assertEqual(g.Session.OAuthScopes, [])
        self.assertEqual(g.Session.AcceptedOAuthScopes, ["user"])

    def testAddAndRemoveScope(self):
        g = self.getEnterpriseBuilder().OAuth(self.data.token).Build()
        u = g.get_authenticated_user()
        self.assertEqual(u.location, "Greece")

        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            u.edit(location="The Moon")

        a = self.electra.get_authenticated_user().get_authorization(self.data.id)
        a.edit(add_scopes=["user"])
        self.pause()

        u.edit(location="The Moon")
        self.assertEqual(u.location, "The Moon")
        u.edit(location="Greece")
        self.assertEqual(u.location, "Greece")
        self.assertEqual(g.Session.OAuthScopes, ["user"])

        a.edit(remove_scopes=["user"])
        self.pause()

        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            u.edit(location="The Moon")


class ApplicationAuthTestCase(TestCase):
    def testGetUser(self):
        g = self.getEnterpriseBuilder().Application("dfb1584c2c0674284875", "16a529070ec817d87e5b186d966fa935bfad1575").Build()  # Create application manually as electra
        self.assertEqual(g.get_user("electra").name, "Electra")

    def testGetSomethingWithQueryParameters(self):
        g = self.getEnterpriseBuilder().Application("dfb1584c2c0674284875", "16a529070ec817d87e5b186d966fa935bfad1575").Build()  # Create application manually as electra
        self.assertIsInstance(g.get_user("electra").get_repos(per_page=2)[0], PyGithub.Blocking.Repository.Repository)

    def testGetAuthenticatedUser(self):
        g = self.getEnterpriseBuilder().Application("dfb1584c2c0674284875", "16a529070ec817d87e5b186d966fa935bfad1575").Build()  # Create application manually as electra
        with self.assertRaises(PyGithub.Blocking.UnauthorizedException):
            self.assertEqual(g.get_authenticated_user().name, "Electra")
