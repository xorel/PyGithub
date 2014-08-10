# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GithubEntities(TestCase):
    @Enterprise("electra")
    def testGetOrg(self):
        o = self.g.get_org("olympus")
        self.assertEqual(o.billing_email, "ghe-olympus@jacquev6.net")

    @Enterprise("electra")
    def testGetUser(self):
        u = self.g.get_user("zeus")
        self.assertEqual(u.name, "Zeus, god of the sky")

    @Enterprise("electra")
    def testGetAuthenticatedUser(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.name, "Electra")

    @Enterprise("zeus")
    def testGetTeam(self):
        t = self.g.get_team(73)
        self.assertEqual(t.name, "Humans")

    @Enterprise("electra")
    def testGetUsers(self):
        users = self.g.get_users()
        self.assertEqual([u.login for u in users], ["ghost", "github-enterprise", "zeus", "poseidon", "morpheus", "antigone", "electra", "penelope", "olympus", "underground"])
        self.assertIsInstance(users[0], PyGithub.Blocking.User.User)
        self.assertIsInstance(users[1], PyGithub.Blocking.Organization.Organization)

    @Enterprise("electra")
    def testGetUsers_allParameters(self):
        users = self.g.get_users(since=16)
        self.assertEqual([u.login for u in users], ["penelope", "olympus", "underground"])
        self.assertEqual(users[0].id, 17)

    @DotCom
    def testGetUsers_pagination(self):
        users = self.g.get_users()[:250]
        self.assertEqual(len(users), 250)


class GithubGists(TestCase):
    @Enterprise("electra")
    def testCreateAnonymousGist(self):
        g = self.g.create_anonymous_gist(files={"foo.txt": {"content": "barbaz"}})
        self.assertEqual(g.owner, None)
        self.assertEqual(g.user, None)
        self.assertEqual(g.public, False)
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            g.delete()

    @Enterprise("electra")
    def testCreateAnonymousGist_allParameters(self):
        g = self.g.create_anonymous_gist(files={"foo.txt": {"content": "barbaz"}}, description="Created by PyGithub", public=True)
        self.assertEqual(g.owner, None)
        self.assertEqual(g.user, None)
        self.assertEqual(g.description, "Created by PyGithub")
        self.assertEqual(g.public, True)
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            g.delete()

    @Enterprise("zeus")
    def testGetGist(self):
        g = self.g.get_gist("3f784a17f0b5851efeee")
        self.assertEqual(g.description, "Immutable gist")

    @Enterprise("zeus")
    def testGetPublicGists(self):
        gists = self.g.get_public_gists()
        self.assertEqual([g.description for g in gists], ["Created by PyGithub", "Mutable gist 2", "Mutable gist 1", "Immutable gist"])

    @Enterprise("zeus")
    def testGetPublicGists_allParameters(self):
        gists = self.g.get_public_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=2)
        self.assertEqual([g.description for g in gists], ["Created by PyGithub", "Mutable gist 2", "Mutable gist 1", "Immutable gist"])


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

    @Enterprise("electra")
    def testGetGitIgnoreTemplate(self):
        t = self.g.get_gitignore_template("C")
        self.assertEqual(t.name, "C")
        self.maxDiff = None
        self.assertEqual(t.source.split("\n"), [
            "# Object files",
            "*.o",
            "*.ko",
            "*.obj",
            "*.elf",
            "",
            "# Libraries",
            "*.lib",
            "*.a",
            "",
            "# Shared objects (inc. Windows DLLs)",
            "*.dll",
            "*.so",
            "*.so.*",
            "*.dylib",
            "",
            "# Executables",
            "*.exe",
            "*.out",
            "*.app",
            "*.i*86",
            "*.x86_64",
            "*.hex",
            ""
        ])

    @Enterprise("electra")
    def testGetGitIgnoreTemplates(self):
        templates = self.g.get_gitignore_templates()
        self.assertEqual(len(templates), 102)
        self.assertEqual(
            templates[:5],
            [
                "Actionscript",
                "Ada",
                "Agda",
                "Android",
                "AppceleratorTitanium",
            ]
        )
        self.assertEqual(
            templates[-5:],
            [
                "ZendFramework",
                "gcov",
                "nanoc",
                "opencart",
                "stella",
            ]
        )

    @DotCom
    def testGetRateLimit(self):
        r = self.g.get_rate_limit()
        self.assertEqual(r.resources.core.limit, 5000)
        self.assertEqual(r.resources.core.remaining, 5000)
        self.assertEqual(r.resources.core.reset, datetime.datetime(2014, 8, 10, 20, 0, 53))
        self.assertEqual(r.resources.search.limit, 30)
        self.assertEqual(r.resources.search.remaining, 30)
        self.assertEqual(r.resources.search.reset, datetime.datetime(2014, 8, 10, 19, 1, 53))

    @DotCom
    def testGetFreshSessionRateLimits(self):
        self.assertEqual(self.g.Session.RateLimit.remaining, 4999)

    @DotCom
    def testSetSessionRateLimits(self):
        self.g.get_authenticated_user()
        self.assertEqual(self.g.Session.RateLimit.remaining, 4998)

    @DotCom
    def testUpdateSessionRateLimits(self):
        self.assertEqual(self.g.Session.RateLimit.remaining, 4998)
        self.g.get_authenticated_user()
        self.assertEqual(self.g.Session.RateLimit.remaining, 4997)


class GithubRepositories(TestCase):
    @Enterprise("electra")
    def testGetRepo(self):
        r = self.g.get_repo(("electra", "immutable"))
        self.assertEqual(r.full_name, "electra/immutable")

    @Enterprise("electra")
    def testGetRepos(self):
        repos = self.g.get_repos()
        self.assertEqual([r.full_name for r in repos], ["/repo-user-1-1", "/repo-user-1-1", "/repo-org-1-1", "/repo-user-1-ephemeral", "/repo-user-1-1", "olympus/trojan-war", "olympus/trojan-war", "olympus/trojan-war", "olympus/trojan-war", "electra/issues", "electra/pulls", "penelope/pulls", "electra/immutable", "olympus/immutable", "penelope/immutable", "electra/contributors", "electra/mutable", "electra/issues", "penelope/mutable", "electra/ephemeral", "olympus/org-repo", "electra/git-objects", "zeus/immutable"])

    @Enterprise("electra")
    def testGetRepos_allParameters(self):
        repos = self.g.get_repos(since=68)
        self.assertEqual([r.full_name for r in repos], ["electra/ephemeral", "olympus/org-repo", "electra/git-objects", "zeus/immutable"])

    @DotCom
    def testGetRepos_pagination(self):
        repos = self.g.get_repos()[:250]
        self.assertEqual(len(repos), 250)
