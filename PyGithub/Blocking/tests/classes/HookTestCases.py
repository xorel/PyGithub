# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class HookAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "hook-attributes")
        h = repo.create_hook("twitter", dict(token="foobar", secret="barbaz", digest=False, short_format=True), events=["push", "commit_comment"])
        return Data(id=h.id)

    def test(self):
        h = self.electra.get_repo(("electra", "hook-attributes")).get_hook(self.data.id)
        self.assertEqual(h.active, True)
        self.assertEqual(h.config, dict(token="foobar", secret="barbaz", digest="false", short_format="true"))
        self.assertEqual(h.created_at, datetime.datetime(2014, 8, 23, 5, 45, 42))
        self.assertEqual(h.events, ["push", "commit_comment"])
        self.assertEqual(h.id, 9)
        self.assertEqual(h.last_response.code, None)
        self.assertEqual(h.last_response.message, None)
        self.assertEqual(h.last_response.status, "unused")
        self.assertEqual(h.name, "twitter")
        self.assertEqual(h.test_url, "http://github.home.jacquev6.net/api/v3/repos/electra/hook-attributes/hooks/9/test")
        self.assertEqual(h.updated_at, datetime.datetime(2014, 8, 23, 5, 45, 42))
        self.assertEqual(h.url, "http://github.home.jacquev6.net/api/v3/repos/electra/hook-attributes/hooks/9")


class HookEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "hook-edit")
        h = repo.create_hook("twitter", dict(token="foobar", secret="barbaz", digest=False, short_format=True))
        h.edit(config=dict(token="foobar", secret="barbaz", digest=False, short_format=True))
        return Data(id=h.id)

    def testConfig(self):
        h = self.electra.get_repo(("electra", "hook-edit")).get_hook(self.data.id)
        self.assertEqual(h.config, dict(token="foobar", secret="barbaz", digest="0", short_format="1"))
        h.edit(config=dict(token="xxx", secret="yyy", digest=True, short_format=False))
        self.assertEqual(h.config, dict(token="xxx", secret="yyy", digest="1", short_format="0"))
        h.edit(config=dict(token="foobar", secret="barbaz", digest=False, short_format=True))
        self.assertEqual(h.config, dict(token="foobar", secret="barbaz", digest="0", short_format="1"))

    def testActive(self):
        h = self.electra.get_repo(("electra", "hook-edit")).get_hook(self.data.id)
        self.assertEqual(h.active, True)
        h.edit(active=False)
        self.assertEqual(h.active, False)
        h.edit(active=True)
        self.assertEqual(h.active, True)

    def testScopes(self):
        h = self.electra.get_repo(("electra", "hook-edit")).get_hook(self.data.id)
        self.assertEqual(h.events, ["push"])
        h.edit(events=["issues", "member"])
        self.assertEqual(h.events, ["issues", "member"])
        h.edit(add_events=["push", "public"])
        self.assertEqual(h.events, ["issues", "member", "push", "public"])
        h.edit(remove_events=["public", "issues", "member"])
        self.assertEqual(h.events, ["push"])


class HookTesting(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "hook-testing")
        return Data()

    def testTest(self):
        repo = self.electra.get_repo(("electra", "hook-testing"))
        i = repo.create_hook("twitter", dict(token="foobar", secret="barbaz", digest=False, short_format=True)).id
        self.pause()
        h = repo.get_hook(i)
        self.assertEqual(h.last_response.code, None)
        self.assertEqual(h.last_response.message, None)
        self.assertEqual(h.last_response.status, "unused")
        h.test()
        self.pause(15)
        self.assertTrue(h.update())
        self.assertEqual(h.last_response.code, 200)
        self.assertEqual(h.last_response.message, "OK")
        self.assertEqual(h.last_response.status, "active")
        self.assertFalse(h.update())
        h.delete()

    def testPing(self):
        repo = self.electra.get_repo(("electra", "hook-testing"))
        i = repo.create_hook("twitter", dict(token="foobar", secret="barbaz", digest=False, short_format=True)).id
        self.pause()
        h = repo.get_hook(i)
        self.assertEqual(h.last_response.code, None)
        self.assertEqual(h.last_response.message, None)
        self.assertEqual(h.last_response.status, "unused")
        h.ping()
        self.pause(15)
        self.assertTrue(h.update())
        self.assertEqual(h.last_response.code, 200)
        self.assertEqual(h.last_response.message, "twitter Service does not respond to :ping events")
        self.assertEqual(h.last_response.status, "active")
        self.assertFalse(h.update())
        h.delete()
