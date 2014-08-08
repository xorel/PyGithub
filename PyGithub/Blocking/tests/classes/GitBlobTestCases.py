# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GitBlobAttributes(TestCase):
    @Enterprise("electra")
    def test(self):
        b = self.g.get_repo(("electra", "git-objects")).get_git_blob("3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(b.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
        self.assertEqual(b.encoding, "base64")
        self.assertEqual(b.mode, None)
        self.assertEqual(b.path, None)
        self.assertEqual(b.size, 20)
        self.assertEqual(b.type, None)

    @Enterprise("electra")
    def testInTree(self):
        b = self.g.get_repo(("electra", "git-objects")).get_git_tree("a3c1d7475466e7d87f8ac38a0001b5548014ba62").tree[0]
        self.assertEqual(b.mode, "100644")
        self.assertEqual(b.path, "a_blob")
        self.assertEqual(b.type, "blob")


class GitBlobUpdate(TestCase):
    @Enterprise("electra")
    def testThroughLazyCompletion(self):
        b = self.g.get_repo(("electra", "git-objects")).create_git_blob("This is some content", "utf8")
        self.assertEqual(b.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(b.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
