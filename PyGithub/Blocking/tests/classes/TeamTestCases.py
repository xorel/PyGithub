# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class TeamAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        reset = False
        o = self.electra.get_org("teamss")  # Create manually as electra
        teams = list(o.get_teams())
        for t in teams:
            if t.name == "attributes":
                t.delete()
        attributes = o.create_team("attributes")
        return Data(id=attributes.id)

    def test(self):
        t = self.electra.get_team(self.data.id)
        self.assertEqual(t.id, 88)
        self.assertEqual(t.members_count, 0)
        self.assertEqual(t.members_url, "http://github.home.jacquev6.net/api/v3/teams/88/members{/member}")
        self.assertEqual(t.name, "attributes")
        self.assertEqual(t.organization.login, "teamss")
        self.assertEqual(t.permission, "pull")
        self.assertEqual(t.repos_count, 0)
        self.assertEqual(t.repositories_url, "http://github.home.jacquev6.net/api/v3/teams/88/repos")
        self.assertEqual(t.slug, "attributes")
        self.assertEqual(t.url, "http://github.home.jacquev6.net/api/v3/teams/88")


class TeamDelete(TestCase):
    def test(self):
        o = self.electra.get_org("teamss")  # Create manually as electra
        t = o.create_team("ephemeral")
        t.delete()


class TeamEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        reset = False
        o = self.electra.get_org("teamss")  # Create manually as electra
        teams = list(o.get_teams())
        for t in teams:
            if t.name == "edit":
                t.delete()
        edit = o.create_team("edit")
        return Data(id=edit.id)

    def testName(self):
        t = self.electra.get_team(self.data.id)
        self.assertEqual(t.name, "edit")
        t.edit(name="editx!")
        self.assertEqual(t.name, "editx!")
        self.assertEqual(t.slug, "editx")
        t.edit(name="edit")
        self.assertEqual(t.name, "edit")

    def testPermission(self):
        t = self.electra.get_team(self.data.id)
        self.assertEqual(t.permission, "pull")
        t.edit(permission="push")
        self.assertEqual(t.permission, "push")
        t.edit(permission="pull")
        self.assertEqual(t.permission, "pull")


class TeamMembers(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        reset = False
        o = self.electra.get_org("teamss")  # Create manually as electra
        teams = list(o.get_teams())
        for t in teams:
            if t.name == "members":
                t.delete()
        members = o.create_team("members")
        members.add_to_members("antigone")
        members.add_to_members("penelope")
        return Data(id=members.id)

    def testGetMembers(self):
        t = self.electra.get_team(self.data.id)
        members = t.get_members()
        self.assertEqual([m.login for m in members], ["antigone", "penelope"])

    def testGetMembers_allParameters(self):
        t = self.electra.get_team(self.data.id)
        members = t.get_members(per_page=1)
        self.assertEqual([m.login for m in members], ["antigone", "penelope"])

    def testAddToAndRemoveFromMembers(self):
        t = self.electra.get_team(self.data.id)
        self.assertFalse(t.has_in_members("electra"))
        t.add_to_members("electra")
        self.assertTrue(t.has_in_members("electra"))
        t.remove_from_members("electra")
        self.assertFalse(t.has_in_members("electra"))


class TeamRepos(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        reset = False
        o = self.electra.get_org("teamss")  # Create manually as electra
        teams = list(o.get_teams())
        for t in teams:
            if t.name == "repos":
                t.delete()
        repos = o.create_team("repos")
        try:
            repos.add_to_repos(o.get_repo("a"))
        except PyGithub.Blocking.ObjectNotFoundException:
            repos.add_to_repos(o.create_repo("a"))
        try:
            repos.add_to_repos(o.get_repo("b"))
        except PyGithub.Blocking.ObjectNotFoundException:
            repos.add_to_repos(o.create_repo("b"))
        return Data(id=repos.id)

    def testGetRepos(self):
        t = self.electra.get_team(self.data.id)
        repos = t.get_repos()
        self.assertEqual([r.name for r in repos], ["a", "b"])

    def testGetRepos_allParameters(self):
        t = self.electra.get_team(self.data.id)
        repos = t.get_repos(per_page=1)
        self.assertEqual([r.name for r in repos], ["a", "b"])

    def testAddToAndRemoveFromRepos(self):
        t = self.electra.get_team(self.data.id)
        self.assertTrue(t.has_in_repos(("teamss", "b")))
        t.remove_from_repos(("teamss", "b"))
        self.assertFalse(t.has_in_repos(("teamss", "b")))
        t.add_to_repos(("teamss", "b"))
        self.assertTrue(t.has_in_repos(("teamss", "b")))


class TeamUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        reset = False
        o = self.electra.get_org("teamss")  # Create manually as electra
        teams = list(o.get_teams())
        for t in teams:
            if t.name == "update":
                t.delete()
        update = o.create_team("update")
        self.pause()
        return Data(id=update.id)

    def test(self):
        t1 = self.electra.get_team(self.data.id)
        t2 = self.electra.get_team(self.data.id)
        t2.edit(name="updatex!")
        self.pause()
        self.assertEqual(t1.name, "update")
        self.assertTrue(t1.update())
        self.assertEqual(t1.name, "updatex!")
        self.assertFalse(t1.update())
        t2.edit(name="update")
