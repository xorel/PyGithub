# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GistAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        source = self.electra.get_authenticated_user().create_gist(files={"foo.txt": {"content": "barbaz"}, "bar.txt": {"content": "tartempion"}}, public=True, description="attributes")
        fork = self.penelope.get_authenticated_user().create_gist_fork(source.id)
        fork.edit(files={"new.txt": {"content": "added"}})
        self.zeus.get_authenticated_user().create_gist_fork(source.id)
        return Data(sourceId=source.id, forkId=fork.id)

    def testSourceAttributes(self):
        g = self.electra.get_gist(self.data.sourceId)
        self.assertEqual(g.comments, 0)
        self.assertEqual(g.comments_url, "http://github.home.jacquev6.net/api/v3/gists/a6a7bf0c2a37e429e4ff/comments")
        self.assertEqual(g.commits_url, "http://github.home.jacquev6.net/api/v3/gists/a6a7bf0c2a37e429e4ff/commits")
        self.assertEqual(g.created_at, datetime.datetime(2014, 8, 15, 5, 29, 0))
        self.assertEqual(g.description, "attributes")
        self.assertEqual(len(g.files), 2)
        self.assertEqual(g.files["foo.txt"].content, "barbaz")
        self.assertEqual(g.files["foo.txt"].filename, "foo.txt")
        self.assertEqual(g.files["foo.txt"].language, None)
        self.assertEqual(g.files["foo.txt"].raw_url, "http://github.home.jacquev6.net/gist/electra/a6a7bf0c2a37e429e4ff/raw/4b498a6ddbe47a306db2b75e79c19d4228c6f1bf/foo.txt")
        self.assertEqual(g.files["foo.txt"].size, 6)
        self.assertEqual(g.files["foo.txt"].truncated, False)
        self.assertEqual(g.files["foo.txt"].type, "text/plain")
        self.assertEqual(g.fork_of, None)
        self.assertEqual(len(g.forks), 2)
        self.assertEqual(g.forks[0].user.login, "penelope")  # Yes, not owner, weird
        self.assertEqual(g.forks_url, "http://github.home.jacquev6.net/api/v3/gists/a6a7bf0c2a37e429e4ff/forks")
        self.assertEqual(g.git_pull_url, "http://github.home.jacquev6.net/gist/a6a7bf0c2a37e429e4ff.git")
        self.assertEqual(g.git_push_url, "http://github.home.jacquev6.net/gist/a6a7bf0c2a37e429e4ff.git")
        self.assertEqual(len(g.history), 1)
        self.assertEqual(g.history[0].change_status.additions, 2)
        self.assertEqual(g.history[0].change_status.deletions, 0)
        self.assertEqual(g.history[0].change_status.total, 2)
        self.assertEqual(g.history[0].committed_at, datetime.datetime(2014, 8, 15, 5, 29, 0))
        self.assertEqual(g.history[0].url, "http://github.home.jacquev6.net/api/v3/gists/a6a7bf0c2a37e429e4ff/0aa216744e08f76e6b86fc1c2ab519654ccfb0ff")
        self.assertEqual(g.history[0].user.login, "electra")
        self.assertEqual(g.history[0].version, "0aa216744e08f76e6b86fc1c2ab519654ccfb0ff")
        self.assertEqual(g.html_url, "http://github.home.jacquev6.net/gist/a6a7bf0c2a37e429e4ff")
        self.assertEqual(g.id, "a6a7bf0c2a37e429e4ff")
        self.assertEqual(g.owner.login, "electra")
        self.assertEqual(g.public, True)
        self.assertEqual(g.updated_at, datetime.datetime(2014, 8, 15, 5, 29, 1))
        self.assertEqual(g.user, None)

    def testForkAttributes(self):
        g = self.penelope.get_gist(self.data.forkId)
        self.assertEqual(g.fork_of.id, "a6a7bf0c2a37e429e4ff")
        self.assertEqual(len(g.files), 3)

    def testGetCommits(self):
        commits = list(self.electra.get_gist(self.data.forkId).get_commits())
        self.assertEqual(len(commits), 2)
        self.assertEqual(commits[0].user.login, "penelope")
        self.assertEqual(commits[1].change_status.additions, 2)
        self.assertEqual(commits[1].committed_at, datetime.datetime(2014, 8, 15, 5, 29, 0))
        self.assertEqual(commits[1].url, "http://github.home.jacquev6.net/api/v3/gists/482fa136eb3fd434702b/0aa216744e08f76e6b86fc1c2ab519654ccfb0ff")
        self.assertEqual(commits[1].user.login, "electra")
        self.assertEqual(commits[1].version, "0aa216744e08f76e6b86fc1c2ab519654ccfb0ff")

    def testGetCommits_allParameters(self):
        commits = self.electra.get_gist(self.data.forkId).get_commits(per_page=1)
        # @todoSomeday Consider opening an issue to GitHub because no link is returned. Or consider implementing page += 1 in PaginatedList?
        self.assertEqual([c.user.login for c in commits], ["penelope"])

    def testGetForks(self):
        forks = self.electra.get_gist(self.data.sourceId).get_forks()
        self.assertEqual([f.owner.login for f in forks], ["penelope", "zeus"])

    def testGetForks_allParameters(self):
        forks = self.electra.get_gist(self.data.sourceId).get_forks(per_page=1)
        self.assertEqual([f.owner.login for f in forks], ["penelope", "zeus"])


class GistEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        g = self.electra.get_authenticated_user().create_gist(files={"foo.txt": {"content": "barbaz"}}, public=True, description="edit")
        return Data(id=g.id)

    def testDescription(self):
        g = self.electra.get_gist(self.data.id)
        self.assertEqual(g.description, "edit")
        g.edit(description="edit!")
        self.assertEqual(g.description, "edit!")
        g.edit(description="edit")
        self.assertEqual(g.description, "edit")

    def testFileContent(self):
        g = self.electra.get_gist(self.data.id)
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["foo.txt"].content, "barbaz")
        g.edit(files={"foo.txt": {"content": "barbar"}})
        g.update()  # @todoSomeday Consider opening ticket to GitHub: response to edit should always contain new files
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["foo.txt"].content, "barbar")
        g.edit(files={"foo.txt": {"content": "barbaz"}})
        g.update()  # Idem
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["foo.txt"].content, "barbaz")

    def testMoveFile(self):
        g = self.electra.get_gist(self.data.id)
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["foo.txt"].content, "barbaz")
        g.edit(files={"foo.txt": {"content": "barbaz", "filename": "moved.txt"}})
        g.update()  # Idem
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["moved.txt"].content, "barbaz")
        g.edit(files={"moved.txt": {"content": "barbaz", "filename": "foo.txt"}})
        g.update()  # Idem
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["foo.txt"].content, "barbaz")

    def testAddRemoveFile(self):
        g = self.electra.get_gist(self.data.id)
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["foo.txt"].content, "barbaz")
        g.edit(files={"new.txt": {"content": "toto"}})
        g.update()  # Idem
        self.assertEqual(len(g.files), 2)
        self.assertEqual(g.files["foo.txt"].content, "barbaz")
        self.assertEqual(g.files["new.txt"].content, "toto")
        g.edit(files={"new.txt": None})
        g.update()  # Idem
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["foo.txt"].content, "barbaz")

# @todoAlpha Newly created objects should be candidate for lazy completion: create_gist_fork doesn't return fork_of!


class GistDelete(TestCase):
    def test(self):
        g = self.electra.get_authenticated_user().create_gist(files={"foo.txt": {"content": "barbaz"}}, public=True, description="ephemeral")
        g.delete()
