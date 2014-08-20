# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class CommitCommentAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "commit-comment-attributes")
        commit = repo.get_commits()[0]
        c = commit.create_commit_comment("a", "README.md", 1)
        self.pause()
        return Data(id=c.id)

    def test(self):
        c = self.electra.get_repo(("electra", "commit-comment-attributes")).get_commit_comment(self.data.id)
        self.assertEqual(c.body, "a")
        self.assertEqual(c.body_html, "<p>a</p>")
        self.assertEqual(c.body_text, "a")
        self.assertEqual(c.commit_id, "b7a9d5f6fc613900c52f25b0f9ccedbd61d87f49")
        self.assertEqual(c.created_at, datetime.datetime(2014, 8, 20, 3, 30, 28))
        self.assertEqual(c.html_url, "http://github.home.jacquev6.net/electra/commit-comment-attributes/commit/b7a9d5f6fc613900c52f25b0f9ccedbd61d87f49#commitcomment-10")
        self.assertEqual(c.id, 10)
        self.assertEqual(c.line, None)
        self.assertEqual(c.path, "README.md")
        self.assertEqual(c.position, 1)
        self.assertEqual(c.updated_at, datetime.datetime(2014, 8, 20, 3, 30, 28))
        self.assertEqual(c.url, "http://github.home.jacquev6.net/api/v3/repos/electra/commit-comment-attributes/comments/10")
        self.assertEqual(c.user.login, "electra")


class CommitCommentDelete(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "commit-comment-delete")
        return Data()

    def test(self):
        commit = self.electra.get_repo(("electra", "commit-comment-delete")).get_commits()[0]
        c = commit.create_commit_comment("ephemeral", "README.md", 1)
        self.pause()
        c.delete()


class CommitCommentEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "commit-comment-edit")
        commit = repo.get_commits()[0]
        c = commit.create_commit_comment("edit", "README.md", 1)
        self.pause()
        return Data(id=c.id)

    def testBody(self):
        c = self.electra.get_repo(("electra", "commit-comment-edit")).get_commit_comment(self.data.id)
        self.assertEqual(c.body, "edit")
        c.edit(body="edit!")
        self.assertEqual(c.body, "edit!")
        c.edit(body="edit")
        self.assertEqual(c.body, "edit")


class CommitCommentUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "commit-comment-update")
        commit = repo.get_commits()[0]
        c = commit.create_commit_comment("update", "README.md", 1)
        self.pause()
        return Data(id=c.id)

    def test(self):
        repo = self.electra.get_repo(("electra", "commit-comment-update"))
        c1 = repo.get_commit_comment(self.data.id)
        c2 = repo.get_commit_comment(self.data.id)
        c2.edit(body="update!")
        self.assertEqual(c1.body, "update")
        self.assertTrue(c1.update())
        self.assertEqual(c1.body, "update!")
        self.assertFalse(c1.update())
        c2.edit(body="update")
