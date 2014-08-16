# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GitTreeAttributes(TestCase):
    def test(self):
        t = self.electra.get_repo(("electra", "git-objects")).get_git_tree("f2b2248a59b245891a16e7d7eecfd7bd499e4521")
        self.assertEqual(t.mode, None)
        self.assertEqual(t.path, None)
        self.assertEqual(t.sha, "f2b2248a59b245891a16e7d7eecfd7bd499e4521")
        self.assertEqual(len(t.tree), 4)
        self.assertEqual(t.tree[0].path, "a_blob")
        self.assertIsInstance(t.tree[0], PyGithub.Blocking.GitBlob.GitBlob)
        self.assertEqual(t.tree[1].path, "a_submodule")
        self.assertEqual(t.tree[1].mode, "160000")
        self.assertEqual(t.tree[1].sha, "5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(t.tree[1].type, "commit")
        self.assertIsInstance(t.tree[1], PyGithub.Blocking.GitTree.GitTree.GitSubmodule)
        self.assertEqual(t.tree[2].path, "a_symlink")
        self.assertIsInstance(t.tree[2], PyGithub.Blocking.GitBlob.GitBlob)
        self.assertEqual(t.tree[3].path, "a_tree")
        self.assertIsInstance(t.tree[3], PyGithub.Blocking.GitTree.GitTree)
        self.assertEqual(t.type, None)

    def testInTree(self):
        b = self.electra.get_repo(("electra", "git-objects")).get_git_tree("f2b2248a59b245891a16e7d7eecfd7bd499e4521").tree[3]
        self.assertEqual(b.mode, "040000")
        self.assertEqual(b.path, "a_tree")
        self.assertEqual(b.type, "tree")


class GitTreeMisc(TestCase):
    def testCreateModifiedCopy(self):
        t = self.electra.get_repo(("electra", "git-objects")).get_git_tree("65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        modified = t.create_modified_copy(tree=[{"path": "other_test.txt", "mode": "100644", "type": "blob", "content": "Another blob"}])
        self.assertEqual(len(modified.tree), 2)


class GitTreeUpdate(TestCase):
    def testThroughLazyCompletion(self):
        t = self.electra.get_repo(("electra", "git-objects")).get_git_tree("f2b2248a59b245891a16e7d7eecfd7bd499e4521").tree[3]
        self.assertEqual(t.path, "a_tree")
        self.assertEqual(t.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(len(t.tree), 1)
        self.assertEqual(t.path, "a_tree")  # Not lost after lazy completion

    def testArtifical(self):
        # GitSubmodule are always returned completely so there is no other way to cover _updateAttributes
        t = self.electra.get_repo(("electra", "git-objects")).get_git_tree("f2b2248a59b245891a16e7d7eecfd7bd499e4521")
        t.tree[1]._updateAttributes()
