# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GithubEntities(TestCase):
    def testGetOrg(self):
        o = self.electra.get_org("olympus")
        self.assertEqual(o.billing_email, "ghe-olympus@jacquev6.net")

    def testGetUser(self):
        u = self.electra.get_user("zeus")
        self.assertEqual(u.name, "Zeus, god of the sky")

    def testGetAuthenticatedUser(self):
        u = self.electra.get_authenticated_user()
        self.assertEqual(u.name, "Electra")

    def testGetTeam(self):
        t = self.zeus.get_team(73)
        self.assertEqual(t.name, "Humans")

    def testGetUsers(self):
        users = self.electra.get_users()
        self.assertEqual([u.login for u in users], ["ghost", "github-enterprise", "zeus", "poseidon", "morpheus", "antigone", "electra", "penelope", "olympus", "underground"])
        self.assertIsInstance(users[0], PyGithub.Blocking.User.User)
        self.assertIsInstance(users[1], PyGithub.Blocking.Organization.Organization)

    def testGetUsers_allParameters(self):
        users = self.electra.get_users(since=16)
        self.assertEqual([u.login for u in users], ["penelope", "olympus", "underground"])
        self.assertEqual(users[0].id, 17)

    def testGetUsers_pagination(self):
        users = self.dotcom.get_users()[:250]
        self.assertEqual(len(users), 250)


class GithubGists(TestCase):
    def testCreateAnonymousGist(self):
        g = self.electra.create_anonymous_gist(files={"foo.txt": {"content": "barbaz"}})
        self.assertEqual(g.owner, None)
        self.assertEqual(g.user, None)
        self.assertEqual(g.public, False)
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            g.delete()

    def testCreateAnonymousGist_allParameters(self):
        g = self.electra.create_anonymous_gist(files={"foo.txt": {"content": "barbaz"}}, description="Created by PyGithub", public=True)
        self.assertEqual(g.owner, None)
        self.assertEqual(g.user, None)
        self.assertEqual(g.description, "Created by PyGithub")
        self.assertEqual(g.public, True)
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            g.delete()

    def testGetGist(self):
        g = self.zeus.get_gist("3f784a17f0b5851efeee")
        self.assertEqual(g.description, "Immutable gist")

    def testGetPublicGists(self):
        gists = self.zeus.get_public_gists()
        self.assertEqual([g.description for g in gists], ["Created by PyGithub", "Mutable gist 2", "Mutable gist 1", "Immutable gist"])

    def testGetPublicGists_allParameters(self):
        gists = self.zeus.get_public_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=2)
        self.assertEqual([g.description for g in gists], ["Created by PyGithub", "Mutable gist 2", "Mutable gist 1", "Immutable gist"])


class GithubMarkdown(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "github-markdown")
        repo.create_issue("markdown")
        return Data()

    def testRenderMarkdown(self):
        t = self.electra.render_markdown("This **is** cool!")
        self.assertEqual(t, "<p>This <strong>is</strong> cool!</p>")

    def testRenderMarkdown_allParameters(self):
        t = self.electra.render_markdown("#1 **is** cool!", mode="gfm", context="electra/github-markdown")
        self.assertEqual(t, '<p><a href="http://github.home.jacquev6.net/electra/github-markdown/issues/1" class="issue-link" title="markdown">#1</a> <strong>is</strong> cool!</p>')


class GithubMisc(TestCase):
    def testGetHooks(self):
        hooks = self.electra.get_hooks()
        self.assertEqual([h.name for h in hooks[:3]], ["activecollab", "acunote", "agilebench"])

    def testGetHook(self):
        h = self.electra.get_hook("campfire")
        self.assertEqual(h.events, ["push", "pull_request", "issues"])
        self.assertEqual(h.supported_events, ["gollum", "issues", "public", "pull_request", "push"])
        self.assertEqual(h.title, "Campfire")
        self.assertEqual(h.name, "campfire")
        self.assertEqual(h.schema, [["string", "subdomain"], ["string", "room"], ["string", "token"], ["string", "sound"], ["boolean", "master_only"], ["boolean", "play_sound"], ["boolean", "long_url"]])

    def testMeta(self):
        # @todoAlpha Consider making Meta updatable, with a constant url "/meta"
        m = self.dotcom.get_meta()
        self.assertEqual(m.git, ["192.30.252.0/22"])
        self.assertEqual(m.hooks, ["192.30.252.0/22"])
        self.assertEqual(m.verifiable_password_authentication, True)

    def testGetEmojis(self):
        emojis = self.electra.get_emojis()
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

    def testGetGitIgnoreTemplate(self):
        t = self.electra.get_gitignore_template("C")
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

    def testGetGitIgnoreTemplates(self):
        templates = self.electra.get_gitignore_templates()
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

    def testGetRateLimit(self):
        r = self.dotcom.get_rate_limit()
        self.assertEqual(r.resources.core.limit, 5000)
        self.assertEqual(r.resources.core.remaining, 5000)
        self.assertEqual(r.resources.core.reset, datetime.datetime(2014, 8, 10, 20, 0, 53))
        self.assertEqual(r.resources.search.limit, 30)
        self.assertEqual(r.resources.search.remaining, 30)
        self.assertEqual(r.resources.search.reset, datetime.datetime(2014, 8, 10, 19, 1, 53))

    def testGetFreshSessionRateLimits(self):
        self.assertEqual(self.dotcom.Session.RateLimit.remaining, 4999)

    def testSetSessionRateLimits(self):
        self.dotcom.get_authenticated_user()
        self.assertEqual(self.dotcom.Session.RateLimit.remaining, 4998)

    def testUpdateSessionRateLimits(self):
        self.assertEqual(self.dotcom.Session.RateLimit.remaining, 4998)
        self.dotcom.get_authenticated_user()
        self.assertEqual(self.dotcom.Session.RateLimit.remaining, 4997)


class GithubRepositories(TestCase):
    def testGetRepo(self):
        r = self.electra.get_repo(("electra", "immutable"))
        self.assertEqual(r.full_name, "electra/immutable")

    def testGetRepos(self):
        repos = self.electra.get_repos()
        self.assertEqual([r.full_name for r in repos], ["/repo-user-1-1", "/repo-user-1-1", "/repo-org-1-1", "/repo-user-1-ephemeral", "/repo-user-1-1", "olympus/trojan-war", "olympus/trojan-war", "olympus/trojan-war", "olympus/trojan-war", "electra/issues", "electra/pulls", "penelope/pulls", "electra/immutable", "olympus/immutable", "penelope/immutable", "electra/contributors", "electra/mutable", "electra/issues", "penelope/mutable", "electra/ephemeral", "olympus/org-repo", "electra/git-objects", "zeus/immutable"])

    def testGetRepos_allParameters(self):
        repos = self.electra.get_repos(since=68)
        self.assertEqual([r.full_name for r in repos], ["electra/ephemeral", "olympus/org-repo", "electra/git-objects", "zeus/immutable"])

    def testGetRepos_pagination(self):
        repos = self.dotcom.get_repos()[:250]
        self.assertEqual(len(repos), 250)


class GithubSearch(TestCase):
    def testSearchUsers(self):
        # @todoAlpha Provide a way to build queries described in https://help.github.com/articles/searching-users
        r = self.electra.search_users("god")
        self.assertEqual(r.total_count, 2)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual([u.login for u in r.items], ["zeus", "poseidon"])

    def testSearchUsers_allParameters(self):
        r = self.electra.search_users("god", sort="joined", order="asc", per_page=1)
        self.assertEqual(r.total_count, 2)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual([u.login for u in r.items], ["zeus", "poseidon"])

    def testSearchUsers_pagination(self):
        r = self.dotcom.search_users("vincent", per_page=100)
        self.assertEqual(r.total_count, 3475)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual(len(list(r.items)), 1000)
        self.assertEqual(r.items[6].login, "jacquev6")
        self.assertEqual(r.items[999].login, "williewillus")

    def testSearchRepositories(self):
        # @todoAlpha Provide a way to build queries described in https://help.github.com/articles/searching-repositories
        r = self.dotcom.search_repositories("GitHub API v3")
        self.assertEqual(r.total_count, 127)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual(r.items[6].full_name, "jacquev6/PyGithub")

    def testSearchRepositories_allParameters(self):
        r = self.dotcom.search_repositories("GitHub API v3", sort="stars", order="desc", per_page=4)
        self.assertEqual(r.total_count, 127)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual(r.items[1].full_name, "jacquev6/PyGithub")
        self.assertEqual(r.items[6].full_name, "farnoy/github-api-client")

    def testSearchIssues(self):
        # @todoAlpha Provide a way to build queries described in https://help.github.com/articles/searching-issues
        # @todoSomeday Consider opening issue to GitHub to return repository as part of issues here, like in AuthenticatedUser.get_user_issues
        r = self.dotcom.search_issues("GitHub API v3")
        self.assertEqual(r.total_count, 6435)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual(r.items[0].title, "Implement GitHub API v3")

    def testSearchIssues_allParameters(self):
        r = self.dotcom.search_issues("GitHub API v3", sort="comments", order="desc", per_page=4)
        self.assertEqual(r.total_count, 6435)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual(r.items[6].title, "v3 feedback")

    def testSearchCode(self):
        # @todoAlpha Provide a way to build queries described in https://help.github.com/articles/searching-code
        r = self.dotcom.search_code("marbles user:jacquev6")
        self.assertEqual(r.total_count, 6)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual(r.items[0].name, "README.md")

    def testSearchCode_allParameters(self):
        # @todoAlpha Provide a way to build queries described in https://help.github.com/articles/searching-code
        r = self.dotcom.search_code("marbles user:jacquev6", sort="indexed", order="asc", per_page=2)
        self.assertEqual(r.total_count, 6)
        self.assertEqual(r.incomplete_results, False)
        self.assertEqual(r.items[3].name, "test.cpp")
