# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *

# @todoAlpha Test this with unit tests in PaginationTestCases.py (when we have a PaginationTestCases.py...)


class PaginationTestCase(TestCase):
    def testIterationOnMultiplePages(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(list(stargazers)), 315)

    def testIterationOnSlice(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual([u.login for u in stargazers[27:33]], ["amokan", "goliatone", "cyraxjoe", "zoni", "dalejung", "reubano"])

    def testIndexAccess(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(stargazers[42].login, "jandersonfc")

    def testIterationOnReversedSlice(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual([u.login for u in stargazers[32:26:-1]], ["reubano", "dalejung", "zoni", "cyraxjoe", "goliatone", "amokan"])

    def testIterationOnSliceWithGaps(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual([u.login for u in stargazers[27:33:2]], ["amokan", "cyraxjoe", "dalejung"])

    def testIterationOnReversedSliceWithGaps(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual([u.login for u in stargazers[32:26:-2]], ["reubano", "zoni", "goliatone"])

    def testFullReversedIteration(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()[::-1]
        self.assertEqual(stargazers[0].login, "alfishe")
        self.assertEqual(stargazers[314].login, "ybakos")

    def testFullReversedIterationWithGaps(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()[::-2]
        self.assertEqual(stargazers[0].login, "alfishe")
        self.assertEqual(stargazers[157].login, "ybakos")

    def testIterationOfUnboundedSlice(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(stargazers[280:]), 35)

    def testIterationOfUnboundedSlice2(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(stargazers[:35]), 35)

    def testIterationOfUnboundedSlice3(self):
        repo = self.dotcom.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(stargazers[:]), 315)

    def testStopIterationOnEmptyPage(self):
        gists = self.dotcom.get_public_gists(since=datetime.datetime(2014, 7, 12, 2, 30, 0), per_page=10)
        self.assertEqual(len(gists[:]), 32)


class PaginationWithGlobalPerPageTestCase(TestCase):
    def testIterationOnMultiplePages(self):
        g = self.getBuilder().Login(DotComLogin, DotComPassword).PerPage(100).Build()
        repo = g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(list(stargazers)), 321)
