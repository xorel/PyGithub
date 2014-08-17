# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class SubmoduleAttributes(TestCase):
    def testWithoutDotGitmodules(self):
        s = self.electra.get_repo(("electra", "git-objects")).get_contents("a_submodule", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertEqual(s.git_url, None)
        self.assertEqual(s.html_url, None)
        self.assertEqual(s.name, "a_submodule")
        self.assertEqual(s.path, "a_submodule")
        self.assertEqual(s.sha, "5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(s.size, 0)
        self.assertEqual(s.submodule_git_url, None)
        self.assertEqual(s.type, "submodule")


class SubmoduleUpdate(TestCase):
    def testLazyCompletion(self):
        s = self.electra.get_repo(("electra", "git-objects")).get_contents("", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")[1]
        self.assertEqual(s.submodule_git_url, None)

    def testAddDotGitmodules(self):
        repo = self.electra.get_repo(("electra", "git-objects"))
        ref = repo.create_git_ref("refs/heads/ephemeral", "db09e03a13f7910b9cae93ca91cd35800e15c695")
        s = repo.get_contents("a_submodule", ref="ephemeral")
        repo.create_file(".gitmodules", "Add .gitmodules", "W3N1Ym1vZHVsZSAiYV9zdWJtb2R1bGUiXQ0KICAgIHBhdGggPSBhX3N1Ym1vZHVsZQ0KICAgIHVybCA9IGh0dHA6Ly9naXRodWIuaG9tZS5qYWNxdWV2Ni5uZXQvZWxlY3RyYS9pbW11dGFibGUuZ2l0DQo=", branch="ephemeral")
        self.pause()
        self.assertTrue(s.update())
        self.assertEqual(s.git_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/trees/5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(s.html_url, "http://github.home.jacquev6.net/electra/immutable/tree/5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(s.submodule_git_url, "http://github.home.jacquev6.net/electra/immutable.git")
        ref.delete()
