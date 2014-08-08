# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GithubMisc(TestCase):
    @Enterprise("electra")
    def testGetHooks(self):
        hooks = self.g.get_hooks()
        self.assertEqual([h.name for h in hooks[:3]], ["activecollab", "acunote", "agilebench"])

    @Enterprise("electra")
    def testGetHook(self):
        h = self.g.get_hook("campfire")
        self.assertEqual(h.events, ["push", "pull_request", "issues"])
        self.assertEqual(h.supported_events, ["gollum", "issues", "public", "pull_request", "push"])
        self.assertEqual(h.title, "Campfire")
        self.assertEqual(h.name, "campfire")
        self.assertEqual(h.schema, [["string", "subdomain"], ["string", "room"], ["string", "token"], ["string", "sound"], ["boolean", "master_only"], ["boolean", "play_sound"], ["boolean", "long_url"]])

    @DotCom
    def testMeta(self):
        # @todoAlpha Consider making Meta updatable, with a constant url "/meta"
        m = self.g.get_meta()
        self.assertEqual(m.git, ["192.30.252.0/22"])
        self.assertEqual(m.hooks, ["192.30.252.0/22"])
        self.assertEqual(m.verifiable_password_authentication, True)

    @Enterprise("electra")
    def testGetEmojis(self):
        emojis = self.g.get_emojis()
        self.assertEqual(len(emojis), 887)
        for k, v in {
            "+1": "http://github.home.jacquev6.net/images/icons/emoji/+1.png?v5",
            "-1": "http://github.home.jacquev6.net/images/icons/emoji/-1.png?v5",
            "100": "http://github.home.jacquev6.net/images/icons/emoji/100.png?v5",
            "1234": "http://github.home.jacquev6.net/images/icons/emoji/1234.png?v5",
            "8ball": "http://github.home.jacquev6.net/images/icons/emoji/8ball.png?v5",
            "yen": "http://github.home.jacquev6.net/images/icons/emoji/yen.png?v5",
            "yum": "http://github.home.jacquev6.net/images/icons/emoji/yum.png?v5",
            "zap": "http://github.home.jacquev6.net/images/icons/emoji/zap.png?v5",
            "zero": "http://github.home.jacquev6.net/images/icons/emoji/zero.png?v5",
            "zzz": "http://github.home.jacquev6.net/images/icons/emoji/zzz.png?v5",
        }.iteritems():
            self.assertEqual(emojis[k], v)
