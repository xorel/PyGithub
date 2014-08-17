# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class CommitAttributes(TestCase):
    def test(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_commit("db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertEqual(c.author, None)
        self.assertEqual(c.comments_url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/commits/db09e03a13f7910b9cae93ca91cd35800e15c695/comments")
        self.assertEqual(c.commit.url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/git/commits/db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertEqual(c.committer, None)
        self.assertEqual(len(c.files), 4)
        self.assertEqual(c.files[3].additions, 1)
        self.assertEqual(c.files[3].blob_url, "http://github.home.jacquev6.net/electra/git-objects/blob/db09e03a13f7910b9cae93ca91cd35800e15c695/a_tree/test.txt")
        self.assertEqual(c.files[3].changes, 1)
        self.assertEqual(c.files[3].contents_url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/contents/a_tree/test.txt?ref=db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertEqual(c.files[3].deletions, 0)
        self.assertEqual(c.files[3].filename, "a_tree/test.txt")
        self.assertEqual(c.files[3].patch, "@@ -0,0 +1 @@\n+This is some content\n\\ No newline at end of file")
        self.assertEqual(c.files[3].raw_url, "http://github.home.jacquev6.net/electra/git-objects/raw/db09e03a13f7910b9cae93ca91cd35800e15c695/a_tree/test.txt")
        self.assertEqual(c.files[3].sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(c.files[3].status, "added")
        self.assertEqual(c.html_url, "http://github.home.jacquev6.net/electra/git-objects/commit/db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertEqual(len(c.parents), 1)
        self.assertEqual(c.parents[0].html_url, "http://github.home.jacquev6.net/electra/git-objects/commit/f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(c.parents[0].sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(c.parents[0].url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/commits/f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(c.sha, "db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertEqual(c.stats.additions, 3)
        self.assertEqual(c.stats.deletions, 0)
        self.assertEqual(c.stats.total, 3)
        self.assertEqual(c.url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/commits/db09e03a13f7910b9cae93ca91cd35800e15c695")


class CommitStatuses(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "commit-statuses")
        commit = repo.get_commits()[0]
        commit.create_status("success", "http://foo.com", "My first status")
        self.pause()
        commit.create_status("pending", "http://bar.com", "My second status")
        self.pause()
        cc = repo.create_file("foo.txt", "Create file", "Zm9vYmFy")
        return Data(sha=commit.sha, otherSha=cc.commit.sha)

    def testGetStatuses(self):
        c = self.electra.get_repo(("electra", "commit-statuses")).get_commit(self.data.sha)
        statuses = c.get_statuses()
        self.assertEqual([s.description for s in statuses], ["My second status", "My first status"])
        self.assertEqual(statuses[0].created_at, datetime.datetime(2014, 8, 17, 4, 43, 24))
        self.assertEqual(statuses[0].creator.login, "electra")
        self.assertEqual(statuses[0].description, "My second status")
        self.assertEqual(statuses[0].id, 10)
        self.assertEqual(statuses[0].state, "pending")
        self.assertEqual(statuses[0].target_url, "http://bar.com")
        self.assertEqual(statuses[0].updated_at, datetime.datetime(2014, 8, 17, 4, 43, 24))
        # status.url is in fact the url of a collection of statuses
        self.assertEqual(statuses[0].url, "http://github.home.jacquev6.net/api/v3/repos/electra/commit-statuses/statuses/a74e609f4d12a526611ff1fcc7d4ddef2bdafa00")

    def testGetStatuses_allParameters(self):
        c = self.electra.get_repo(("electra", "commit-statuses")).get_commit(self.data.sha)
        statuses = c.get_statuses(per_page=1)
        self.assertEqual([s.description for s in statuses], ["My second status", "My first status"])

    def testCreateStatus(self):
        c = self.electra.get_repo(("electra", "commit-statuses")).get_commit(self.data.otherSha)
        s = c.create_status("failure")
        self.assertEqual(s.state, "failure")
        self.assertEqual(s.target_url, None)
        self.assertEqual(s.description, None)

    def testCreateStatus_allParameters(self):
        c = self.electra.get_repo(("electra", "commit-statuses")).get_commit(self.data.otherSha)
        s = c.create_status("error", "http://baz.com", "My third status")
        self.assertEqual(s.state, "error")
        self.assertEqual(s.target_url, "http://baz.com")
        self.assertEqual(s.description, "My third status")


class CommitUpdate(TestCase):
    def testThroughLazyCompletion(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_commit("db09e03a13f7910b9cae93ca91cd35800e15c695").parents[0]
        self.assertEqual(c.stats.total, 1)

    def testArtifical(self):
        # Stats and Files are always returned completely so there is no other way to cover _updateAttributes
        c = self.electra.get_repo(("electra", "git-objects")).get_commit("db09e03a13f7910b9cae93ca91cd35800e15c695")
        c.files[3]._updateAttributes()
        c.stats._updateAttributes()
