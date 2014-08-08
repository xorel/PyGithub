# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GitCommitAttributes(TestCase):
    @Enterprise("electra")
    def test(self):
        c = self.g.get_repo(("electra", "git-objects")).get_git_commit("5fee4dd9e5a3b56dac752c191799fcda69ca8b8a")
        self.assertEqual(c.author.date, datetime.datetime(2000, 12, 31, 23, 59, 59))
        self.assertEqual(c.author.name, "John Doe")
        self.assertEqual(c.author.email, "john@doe.com")
        self.assertEqual(c.comment_count, None)
        self.assertEqual(c.committer.date, datetime.datetime(2001, 1, 1, 0, 0))
        self.assertEqual(c.committer.name, "Jane Doe")
        self.assertEqual(c.committer.email, "jane@doe.com")
        self.assertEqual(c.html_url, "http://github.home.jacquev6.net/electra/git-objects/commit/5fee4dd9e5a3b56dac752c191799fcda69ca8b8a")
        self.assertEqual(c.message, "second commit")
        self.assertEqual(len(c.parents), 1)
        self.assertEqual(c.parents[0].sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(c.sha, "5fee4dd9e5a3b56dac752c191799fcda69ca8b8a")
        self.assertEqual(c.tree.sha, "a3c1d7475466e7d87f8ac38a0001b5548014ba62")
        self.assertEqual(c.type, None)


class GitCommitUpdate(TestCase):
    @Enterprise("electra")
    def testThroughLazyCompletion(self):
        c = self.g.get_repo(("electra", "git-objects")).get_git_commit("5fee4dd9e5a3b56dac752c191799fcda69ca8b8a").parents[0]
        self.assertEqual(c.sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(c.tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")

    @Enterprise("electra")
    def testArtifical(self):
        # Author are always returned completely so there is no other way to cover _updateAttributes
        c = self.g.get_repo(("electra", "git-objects")).get_git_commit("5fee4dd9e5a3b56dac752c191799fcda69ca8b8a")
        c.author._updateAttributes()
