# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class ContributorAttributes(TestCase):
    def test(self):
        c = self.electra.get_repo(("electra", "contributors")).get_contributors()[0]
        self.assertEqual(c.contributions, 1)


class ContributorUpdate(TestCase):
    def testUpdatePartialObject(self):
        c = self.electra.get_repo(("electra", "contributors")).get_contributors()[0]
        self.assertTrue(c.update())
        self.assertEqual(c.contributions, 1)

    def testLazyCompletion(self):
        c = self.electra.get_repo(("electra", "contributors")).get_contributors()[0]
        self.assertEqual(c.name, "Electra")
        self.assertEqual(c.contributions, 1)
