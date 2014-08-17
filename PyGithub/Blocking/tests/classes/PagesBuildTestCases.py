# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class PagesBuildAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "pages-build-attributes")
        repo.create_git_ref("refs/heads/gh-pages", repo.get_git_ref("refs/heads/master").object.sha)
        self.pause()
        while repo.get_pages().status != "built":
            self.pause()
        return Data()

    def test(self):
        b = self.electra.get_repo(("electra", "pages-build-attributes")).get_latest_pages_build()
        self.assertEqual(b.commit, "42805dcfacc83605a20f1b69ce31d2c161483045")
        self.assertEqual(b.created_at, datetime.datetime(2014, 8, 17, 6, 8, 49))
        self.assertEqual(b.duration, 5681)
        self.assertEqual(b.error.message, None)
        self.assertEqual(b.pusher.login, "electra")
        self.assertEqual(b.status, "built")
        self.assertEqual(b.updated_at, datetime.datetime(2014, 8, 17, 6, 8, 55))


class PagesBuildUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "pages-build-update")
        repo.create_git_ref("refs/heads/gh-pages", repo.get_git_ref("refs/heads/master").object.sha)
        self.pause()
        while repo.get_pages().status != "built":
            self.pause()
        return Data()

    def test(self):
        repo = self.electra.get_repo(("electra", "pages-build-update"))
        before = repo.get_latest_pages_build()
        repo.create_file("index.html", "Add Index", "SGkgdGhlcmUh", branch="gh-pages")
        after = repo.get_latest_pages_build()
        while after.url == before.url:
            after = repo.get_latest_pages_build()
            self.pause(0.25)
        self.assertEqual(after.updated_at, datetime.datetime(2014, 8, 17, 6, 33, 20))
        while not after.update():
            self.pause(0.25)
        self.assertEqual(after.updated_at, datetime.datetime(2014, 8, 17, 6, 33, 26))
        repo.get_git_ref("refs/heads/gh-pages").edit(sha=repo.get_git_ref("refs/heads/master").object.sha, force=True)
