# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class ContributorAttributes(TestCase):
    def test(self):
        c = self.electra.get_repo(("electra", "contributors")).get_contributors()[0]
        self.assertEqual(c.contributions, 1)
        self.assertEqual(c.url, "http://github.home.jacquev6.net/api/v3/users/electra")


class ContributorUpdate(TestCase):
    def testUpdatePartialObject(self):
        c = self.electra.get_repo(("electra", "contributors")).get_contributors()[0]
        self.assertTrue(c.update())
        self.assertEqual(c.contributions, 1)

    def testLazyCompletion(self):
        c = self.electra.get_repo(("electra", "contributors")).get_contributors()[0]
        self.assertEqual(c.name, "Electra")
        self.assertEqual(c.contributions, 1)

    def testUpdate(self):
        c = self.electra.get_repo(("electra", "contributors")).get_contributors()[0]
        c.name  # To trigger lazy completion
        u = self.electra.get_authenticated_user()
        u.edit(name="Electra!")
        self.pause()
        self.assertEqual(c.name, "Electra")
        self.assertTrue(c.update())
        self.assertEqual(c.name, "Electra!")
        self.assertEqual(c.contributions, 1)
        self.assertFalse(c.update())
        u.edit(name="Electra")
