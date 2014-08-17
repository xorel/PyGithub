# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class PagesInformationAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "pages-information-attributes")
        repo.create_git_ref("refs/heads/gh-pages", repo.get_git_ref("refs/heads/master").object.sha)
        self.pause()
        while repo.get_pages().status != "built":
            self.pause()
        return Data()

    def test(self):
        i = self.electra.get_repo(("electra", "pages-information-attributes")).get_pages()
        self.assertEqual(i.status, "built")
        self.assertEqual(i.cname, None)
        self.assertEqual(i.custom_404, False)


class PagesInformationUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "pages-information-update")
        repo.create_git_ref("refs/heads/gh-pages", repo.get_git_ref("refs/heads/master").object.sha)
        self.pause()
        while repo.get_pages().status != "built":
            self.pause()
        return Data()

    def test(self):
        repo = self.electra.get_repo(("electra", "pages-information-update"))
        i = repo.get_pages()
        self.assertEqual(i.status, "built")
        before = repo.get_latest_pages_build()
        repo.create_file("index.html", "Add Index", "SGkgdGhlcmUh", branch="gh-pages")
        after = repo.get_latest_pages_build()
        while after.url == before.url:
            after = repo.get_latest_pages_build()
            self.pause(0.25)
        i.update()
        self.assertEqual(i.status, "building")
        repo.get_git_ref("refs/heads/gh-pages").edit(sha=repo.get_git_ref("refs/heads/master").object.sha, force=True)
