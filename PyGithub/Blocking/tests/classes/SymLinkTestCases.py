# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class SymLinkAttributes(TestCase):
    @Enterprise("electra")
    def test(self):
        s = self.g.get_repo(("electra", "git-objects")).get_contents("a_symlink", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertEqual(s.git_url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/git/blobs/a643a1219336c8eee2b5552ac1fead85e2641a45")
        self.assertEqual(s.html_url, "http://github.home.jacquev6.net/electra/git-objects/blob/db09e03a13f7910b9cae93ca91cd35800e15c695/a_symlink")
        self.assertEqual(s.name, "a_symlink")
        self.assertEqual(s.path, "a_symlink")
        self.assertEqual(s.sha, "a643a1219336c8eee2b5552ac1fead85e2641a45")
        self.assertEqual(s.size, 7)
        self.assertEqual(s.target, "a_blob\n")
        self.assertEqual(s.type, "symlink")


class SymLinkUpdate(TestCase):
    @Enterprise("electra")
    def testLazyCompletion(self):
        s = self.g.get_repo(("electra", "git-objects")).get_contents("", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")[2]
        self.assertEqual(s.target, "a_blob\n")
