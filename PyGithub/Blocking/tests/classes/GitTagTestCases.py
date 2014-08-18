# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GitTagAttributes(TestCase):
    def test(self):
        t = self.electra.get_repo(("electra", "git-objects")).get_git_tag("b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        self.assertEqual(t.message, "This is a tag")
        self.assertEqual(t.object.sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(t.object.type, "commit")
        self.assertIsInstance(t.object, PyGithub.Blocking.GitCommit.GitCommit)
        self.assertEqual(t.sha, "b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        self.assertEqual(t.tag, "heavy-tag")
        self.assertEqual(t.tagger.name, "John Doe")
        self.assertEqual(t.type, None)
        self.assertEqual(t.url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/git/tags/b55a47efb4f8c891b6719a3d85a80c7f875e33ec")


class GitTagUpdate(TestCase):
    def testThroughLazyCompletion(self):
        r = self.electra.get_repo(("electra", "git-objects")).create_git_ref(ref="refs/tests/tag_ref", sha="b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        t = r.object
        self.assertEqual(t.tagger.name, "John Doe")
        r.delete()

    def testWithIncompleteObject(self):
        # Tags are immutable so there is no way to update a complete object
        r = self.electra.get_repo(("electra", "git-objects")).create_git_ref(ref="refs/tests/ephemeral", sha="b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        t = r.object
        self.assertTrue(t.update())
        self.assertEqual(t.tagger.name, "John Doe")
        self.assertFalse(t.update())
        r.delete()
