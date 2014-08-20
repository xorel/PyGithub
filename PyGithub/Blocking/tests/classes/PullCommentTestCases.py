# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class PullCommentAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "pull-comment-attributes")
        repo.create_git_ref("refs/heads/release", repo.get_git_ref("heads/master").object.sha)
        c = repo.get_readme().edit("Merge this", content="WWVhaCEgU28gZ29vZCE=")
        pull = repo.create_pull("comment-attributes", "electra:master", "release")
        c = pull.create_pull_comment("attributes", c.sha, "README.md", 1)
        self.pause()
        return Data(id=c.id)

    def test(self):
        c = self.electra.get_repo(("electra", "pull-comment-attributes")).get_pull_comment(self.data.id)
        self.assertEqual(c.body, "attributes")
        self.assertEqual(c.body_html, "<p>attributes</p>")
        self.assertEqual(c.body_text, "attributes")
        self.assertEqual(c.commit_id, "bba9b584f5a7db92c4e8c2f93f8e5dd4714a09b0")
        self.assertEqual(c.created_at, datetime.datetime(2014, 8, 20, 3, 57, 26))
        self.assertEqual(c.diff_hunk, "@@ -1,2 +1 @@\n-pull-comment-attributes")
        self.assertEqual(c.html_url, "http://github.home.jacquev6.net/electra/pull-comment-attributes/pull/1#discussion_r8")
        self.assertEqual(c.id, 8)
        self.assertEqual(c.original_commit_id, "bba9b584f5a7db92c4e8c2f93f8e5dd4714a09b0")
        self.assertEqual(c.original_position, 1)
        self.assertEqual(c.path, "README.md")
        self.assertEqual(c.position, 1)
        self.assertEqual(c.pull_request_url, "http://github.home.jacquev6.net/api/v3/repos/electra/pull-comment-attributes/pulls/1")
        self.assertEqual(c.updated_at, datetime.datetime(2014, 8, 20, 3, 57, 26))
        self.assertEqual(c.url, "http://github.home.jacquev6.net/api/v3/repos/electra/pull-comment-attributes/pulls/comments/8")
        self.assertEqual(c.user.login, "electra")


class PullCommentDelete(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "pull-comment-delete")
        repo.create_git_ref("refs/heads/release", repo.get_git_ref("heads/master").object.sha)
        c = repo.get_readme().edit("Merge this", content="WWVhaCEgU28gZ29vZCE=")
        repo.create_pull("comment-delete", "electra:master", "release")
        return Data(sha=c.sha)

    def test(self):
        pull = self.electra.get_repo(("electra", "pull-comment-delete")).get_pull(1)
        c = pull.create_pull_comment("ephemeral", self.data.sha, "README.md", 1)
        self.pause()
        c.delete()


class PullCommentEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "pull-comment-edit")
        repo.create_git_ref("refs/heads/release", repo.get_git_ref("heads/master").object.sha)
        c = repo.get_readme().edit("Merge this", content="WWVhaCEgU28gZ29vZCE=")
        pull = repo.create_pull("comment-edit", "electra:master", "release")
        c = pull.create_pull_comment("edit", c.sha, "README.md", 1)
        self.pause()
        return Data(id=c.id)

    def testBody(self):
        c = self.electra.get_repo(("electra", "pull-comment-edit")).get_pull_comment(self.data.id)
        self.assertEqual(c.body, "edit")
        c.edit(body="edit!")
        self.assertEqual(c.body, "edit!")
        c.edit(body="edit")
        self.assertEqual(c.body, "edit")


class PullCommentUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "pull-comment-update")
        repo.create_git_ref("refs/heads/release", repo.get_git_ref("heads/master").object.sha)
        c = repo.get_readme().edit("Merge this", content="WWVhaCEgU28gZ29vZCE=")
        pull = repo.create_pull("comment-update", "electra:master", "release")
        c = pull.create_pull_comment("update", c.sha, "README.md", 1)
        self.pause()
        return Data(id=c.id)

    def test(self):
        repo = self.electra.get_repo(("electra", "pull-comment-update"))
        c1 = repo.get_pull_comment(self.data.id)
        c2 = repo.get_pull_comment(self.data.id)
        c2.edit(body="update!")
        self.assertEqual(c1.body, "update")
        self.assertTrue(c1.update())
        self.assertEqual(c1.body, "update!")
        self.assertFalse(c1.update())
        c2.edit(body="update")
