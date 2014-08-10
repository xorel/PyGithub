# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.File
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework
from PyGithub.Blocking.tests.Framework import *


class RepositoryTestCase(Framework.SimpleLoginTestCase):
    def testGetStargazers(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_stargazers(per_page=3)
        self.assertEqual(users[0].login, "ybakos")
        self.assertEqual(users[1].login, "huxley")

    def testGetSubscribers(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_subscribers()
        self.assertEqual(users[0].login, "jacquev6")
        self.assertEqual(users[1].login, "equus12")

    def testGetSubscribers_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_subscribers(per_page=3)
        self.assertEqual(users[0].login, "jacquev6")
        self.assertEqual(users[1].login, "equus12")

    def testGetForks(self):
        repos = self.g.get_repo("jacquev6/PyGithub").get_forks()
        self.assertEqual(repos[0].owner.login, "Web5design")
        self.assertEqual(repos[1].owner.login, "pelson")

    def testGetForks_allParameters(self):
        repos = self.g.get_repo("jacquev6/PyGithub").get_forks(sort="stargazers", per_page=3)
        self.assertEqual(repos[0].owner.login, "roverdotcom")
        self.assertEqual(repos[0].stargazers_count, 1)
        self.assertEqual(repos[1].owner.login, "pmuilu")
        self.assertEqual(repos[1].stargazers_count, 1)

    def testGetTeamsOfPersonalRepo(self):
        teams = self.g.get_repo("jacquev6/PyGithub").get_teams()
        self.assertEqual(len(list(teams)), 0)

    def testGetTeamsOfOrgRepo(self):
        teams = self.g.get_repo("BeaverSoftware/FatherBeaver").get_teams()
        self.assertEqual(teams[0].name, "Members")

    def testGetTeams_allParameters(self):
        teams = self.g.get_repo("BeaverSoftware/FatherBeaver").get_teams(per_page=1)
        self.assertEqual(teams[0].name, "Members")

    def testGetKeys(self):
        keys = self.g.get_repo("jacquev6/CodingDojos").get_keys()
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys[0].id, 6941367)

    def testGetKey(self):
        key = self.g.get_repo("jacquev6/CodingDojos").get_key(6941367)
        self.assertEqual(key.title, "dojo@dojo")

    def testCreateKey(self):
        key = self.g.get_repo("jacquev6/CodingDojos").create_key("vincent@test", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkQih2DtSwBzLUtSNYEKULlI5M1qa6vnq42xt9qZpkLav3G9eD/GqJRST+zZMsyfpP62PtiYKXJdLJX2MQIzUgI2PzNy+iMy+ldiTEABYEOCa+BH9+x2R5xXGlmmCPblpamx3kstGtCTa3LSkyIvxbt5vjbXCyThhJaSKyh+42Uedcz7l0y/TODhnkpid/5eiBz6k0VEbFfhM6h71eBdCFpeMJIhGaPTjbKsEjXIK0SRe0v0UQnpXJQkhAINbm+q/2yjt7zwBF74u6tQjRqJK7vQO2k47ZmFMAGeIxS6GheI+JPmwtHkxvfaJjy2lIGX+rt3lkW8xEUxiMTlxeh+0R")
        self.assertEqual(key.id, 7229238)
