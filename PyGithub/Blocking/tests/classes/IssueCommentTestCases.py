# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class CommitCommentAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "issue-comment-attributes")
        issue = repo.create_issue("comment-attributes")
        c = issue.create_issue_comment("attributes")
        self.pause()
        return Data(id=c.id)

    def test(self):
        c = self.electra.get_repo(("electra", "issue-comment-attributes")).get_issue_comment(self.data.id)
        self.assertEqual(c.body, "attributes")
        self.assertEqual(c.body_html, "<p>attributes</p>")
        self.assertEqual(c.body_text, "attributes")
        self.assertEqual(c.created_at, datetime.datetime(2014, 8, 20, 3, 44, 57))
        self.assertEqual(c.html_url, "http://github.home.jacquev6.net/electra/issue-comment-attributes/issues/1#issuecomment-18")
        self.assertEqual(c.id, 18)
        self.assertEqual(c.issue_url, "http://github.home.jacquev6.net/api/v3/repos/electra/issue-comment-attributes/issues/1")
        self.assertEqual(c.updated_at, datetime.datetime(2014, 8, 20, 3, 44, 57))
        self.assertEqual(c.url, "http://github.home.jacquev6.net/api/v3/repos/electra/issue-comment-attributes/issues/comments/18")
        self.assertEqual(c.user.login, "electra")


class CommitCommentDelete(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "issue-comment-delete")
        repo.create_issue("comment-delete")
        return Data()

    def test(self):
        issue = self.electra.get_repo(("electra", "issue-comment-delete")).get_issue(1)
        c = issue.create_issue_comment("ephemeral")
        self.pause()
        c.delete()


class CommitCommentEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "issue-comment-edit")
        issue = repo.create_issue("comment-edit")
        c = issue.create_issue_comment("edit")
        self.pause()
        return Data(id=c.id)

    def testBody(self):
        c = self.electra.get_repo(("electra", "issue-comment-edit")).get_issue_comment(self.data.id)
        self.assertEqual(c.body, "edit")
        c.edit(body="edit!")
        self.assertEqual(c.body, "edit!")
        c.edit(body="edit")
        self.assertEqual(c.body, "edit")


class CommitCommentUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "issue-comment-update")
        issue = repo.create_issue("comment-update")
        c = issue.create_issue_comment("update")
        self.pause()
        return Data(id=c.id)

    def test(self):
        repo = self.electra.get_repo(("electra", "issue-comment-update"))
        c1 = repo.get_issue_comment(self.data.id)
        c2 = repo.get_issue_comment(self.data.id)
        c2.edit(body="update!")
        self.assertEqual(c1.body, "update")
        self.assertTrue(c1.update())
        self.assertEqual(c1.body, "update!")
        self.assertFalse(c1.update())
        c2.edit(body="update")
