# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class AuthenticatedUserAttributes(TestCase):
    @Enterprise("antigone")
    def testEnterpriseUser(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.avatar_url, "http://github.home.jacquev6.net/identicons/9bf31c7ff062936a96d3c8bd1f8f2ff3.png")
        self.assertEqual(u.blog, "http://jacquev6.net/antigone")
        self.assertEqual(u.collaborators, 0)
        self.assertEqual(u.company, "Antigone Software")
        self.assertEqual(u.created_at, datetime.datetime(2014, 8, 2, 16, 54, 38))
        self.assertEqual(u.disk_usage, 0)
        self.assertEqual(u.email, "ghe-antigone@jacquev6.net")
        self.assertEqual(u.events_url, "http://github.home.jacquev6.net/api/v3/users/antigone/events{/privacy}")
        self.assertEqual(u.followers, 0)
        self.assertEqual(u.followers_url, "http://github.home.jacquev6.net/api/v3/users/antigone/followers")
        self.assertEqual(u.following, 0)
        self.assertEqual(u.following_url, "http://github.home.jacquev6.net/api/v3/users/antigone/following{/other_user}")
        self.assertEqual(u.gists_url, "http://github.home.jacquev6.net/api/v3/users/antigone/gists{/gist_id}")
        self.assertEqual(u.gravatar_id, "22204000fcc2173ab585271509092a31")
        self.assertEqual(u.hireable, False)
        self.assertEqual(u.html_url, "http://github.home.jacquev6.net/antigone")
        self.assertEqual(u.id, 15)
        self.assertEqual(u.location, "Greece")
        self.assertEqual(u.login, "antigone")
        self.assertEqual(u.name, "Antigone")
        self.assertEqual(u.organizations_url, "http://github.home.jacquev6.net/api/v3/users/antigone/orgs")
        self.assertEqual(u.owned_private_repos, 0)
        self.assertEqual(u.plan, None)
        self.assertEqual(u.private_gists, 0)
        self.assertEqual(u.public_gists, 0)
        self.assertEqual(u.public_repos, 0)
        self.assertEqual(u.received_events_url, "http://github.home.jacquev6.net/api/v3/users/antigone/received_events")
        self.assertEqual(u.repos_url, "http://github.home.jacquev6.net/api/v3/users/antigone/repos")
        self.assertEqual(u.site_admin, False)
        self.assertEqual(u.starred_url, "http://github.home.jacquev6.net/api/v3/users/antigone/starred{/owner}{/repo}")
        self.assertEqual(u.subscriptions_url, "http://github.home.jacquev6.net/api/v3/users/antigone/subscriptions")
        self.assertEqual(u.suspended_at, None)
        self.assertEqual(u.total_private_repos, 0)
        self.assertEqual(u.type, "User")
        self.assertEqual(u.updated_at, datetime.datetime(2014, 8, 2, 18, 21, 07))


class AuthenticatedUserEdit(TestCase):
    @Enterprise("penelope")
    def testName(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.name, None)
        u.edit(name="Penelope")
        self.assertEqual(u.name, "Penelope")
        u.edit(name=PyGithub.Blocking.Reset)
        self.assertEqual(u.name, None)

    @Enterprise("penelope")
    def testEmail(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.email, None)
        u.edit(email="ghe-penelope@jacquev6.net")
        self.assertEqual(u.email, "ghe-penelope@jacquev6.net")
        u.edit(email=PyGithub.Blocking.Reset)
        self.assertEqual(u.email, None)

    @Enterprise("penelope")
    def testBlog(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.blog, None)
        u.edit(blog="http://jacquev6.net/penelope")
        self.assertEqual(u.blog, "http://jacquev6.net/penelope")
        u.edit(blog=PyGithub.Blocking.Reset)
        self.assertEqual(u.blog, None)

    @Enterprise("penelope")
    def testCompany(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.company, None)
        u.edit(company="Penelope Software")
        self.assertEqual(u.company, "Penelope Software")
        u.edit(company=PyGithub.Blocking.Reset)
        self.assertIsNone(u.company)

    @Enterprise("penelope")
    def testLocation(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.location, None)
        u.edit(location="Greece")
        self.assertEqual(u.location, "Greece")
        u.edit(location=PyGithub.Blocking.Reset)
        self.assertEqual(u.location, None)

    @Enterprise("penelope")
    def testHireable(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.hireable, False)
        u.edit(hireable=PyGithub.Blocking.Reset)
        self.assertIsNone(u.hireable)
        u.edit(hireable=False)
        self.assertEqual(u.hireable, False)


class AuthenticatedUserEmails(TestCase):
    @Enterprise("penelope")
    def testGetEmails(self):
        u = self.g.get_authenticated_user()
        emails = u.get_emails()
        self.assertEqual(len(emails), 1)
        self.assertEqual(emails[0].email, "ghe-penelope@jacquev6.net")
        self.assertEqual(emails[0].primary, True)
        self.assertEqual(emails[0].verified, False)

    @Enterprise("penelope")
    def testAddOneToAndRemoveOneFromEmails(self):
        u = self.g.get_authenticated_user()
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net"])
        u.add_to_emails("foo@bar.com")
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net", "foo@bar.com"])
        u.remove_from_emails("foo@bar.com")
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net"])

    @Enterprise("penelope")
    def testAddSeveralToAndRemoveSeveralFromEmails(self):
        u = self.g.get_authenticated_user()
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net"])
        u.add_to_emails("foo@bar.com", "baz@42.com")
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net", "foo@bar.com", "baz@42.com"])
        u.remove_from_emails("foo@bar.com", "baz@42.com")
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net"])


class AuthenticatedUserFollowing(TestCase):
    @Enterprise("electra")
    def testGetFollowing(self):
        u = self.g.get_authenticated_user()
        following = u.get_following()
        self.assertEqual([f.login for f in following], ["zeus", "poseidon"])

    @Enterprise("electra")
    def testGetFollowing_allParameters(self):
        u = self.g.get_authenticated_user()
        following = u.get_following(per_page=1)
        self.assertEqual([f.login for f in following], ["zeus", "poseidon"])

    @Enterprise("penelope")
    def testAddToAndRemoveFromFollowing(self):
        u = self.g.get_authenticated_user()
        self.assertFalse(u.has_in_following("zeus"))
        u.add_to_following("zeus")
        self.assertTrue(u.has_in_following("zeus"))
        u.remove_from_following("zeus")
        self.assertFalse(u.has_in_following("zeus"))

    @Enterprise("zeus")
    def testGetFollowers(self):
        u = self.g.get_authenticated_user()
        followers = u.get_followers()
        self.assertEqual([f.login for f in followers], ["electra", "poseidon"])

    @Enterprise("zeus")
    def testGetFollowers_allParameters(self):
        u = self.g.get_authenticated_user()
        followers = u.get_followers(per_page=1)
        self.assertEqual([f.login for f in followers], ["electra", "poseidon"])


class AuthenticatedUserGists(TestCase):
    mutableGistId = "8204fee2d7e3f12bde22"

    @Enterprise("electra")
    def testGetGists(self):
        u = self.g.get_authenticated_user()
        gists = u.get_gists()
        self.assertEqual([g.description for g in gists], ["Mutable gist 2", "Mutable gist 1", "Immutable gist"])

    @Enterprise("electra")
    def testGetGists_allParameters(self):
        u = self.g.get_authenticated_user()
        gists = u.get_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([g.description for g in gists], ["Mutable gist 2", "Mutable gist 1", "Immutable gist"])

    @Enterprise("penelope")
    def testGetStarredGists(self):
        u = self.g.get_authenticated_user()
        gists = u.get_starred_gists()
        self.assertEqual([g.description for g in gists], ["Mutable gist 1", "Immutable gist"])

    @Enterprise("penelope")
    def testGetStarredGists_allParameters(self):
        u = self.g.get_authenticated_user()
        gists = u.get_starred_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([g.description for g in gists], ["Mutable gist 1", "Immutable gist"])

    @Enterprise("penelope")
    def testAddToAndRemoveFromStarredGists(self):
        u = self.g.get_authenticated_user()
        self.assertFalse(u.has_in_starred_gists(self.mutableGistId))
        u.add_to_starred_gists(self.mutableGistId)
        self.assertTrue(u.has_in_starred_gists(self.mutableGistId))
        u.remove_from_starred_gists(self.mutableGistId)
        self.assertFalse(u.has_in_starred_gists(self.mutableGistId))

    @Enterprise("penelope")
    def testCreateGistFork(self):
        u = self.g.get_authenticated_user()
        g = u.create_gist_fork(self.mutableGistId)
        self.assertEqual(g.description, "Mutable gist 2")
        self.assertEqual(g.owner.login, "penelope")
        g.delete()

    @Enterprise("electra")
    def testCreateGist(self):
        # @todoAlpha Create input class for files
        u = self.g.get_authenticated_user()
        g = u.create_gist(files={"foo.txt": {"content": "barbaz"}})
        self.assertIsNone(g.description)
        self.assertEqual(g.public, False)
        g.delete()

    @Enterprise("electra")
    def testCreateGist_allParameters(self):
        u = self.g.get_authenticated_user()
        g = u.create_gist(files={"foo.txt": {"content": "barbaz"}, "bar.txt": {"content": "tartempion"}}, public=True, description="Gist created by PyGithub")
        self.assertEqual(g.description, "Gist created by PyGithub")
        self.assertEqual(g.public, True)
        g.delete()


class AuthenticatedUserKeys(TestCase):
    @Enterprise("electra")
    def testGetKeys(self):
        u = self.g.get_authenticated_user()
        keys = u.get_keys()
        self.assertEqual([k.title for k in keys], ["electra-1", "electra-2"])

    @Enterprise("electra")
    def testGetKey(self):
        u = self.g.get_authenticated_user()
        k = u.get_key(4)
        self.assertEqual(k.title, "electra-1")

    @Enterprise("electra")
    def testCreateKey(self):
        u = self.g.get_authenticated_user()
        k = u.create_key("electra-3", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCh/ih0dj35ZIrOSrYIih0ulcIP48H4DMtgLPUfX0BHuknkf9sCtAM+lURjHVsiZNn4mJDQwH0gHZ+NbisN7yKexArffuemvjFVSALlnYXW78SagsrEvAlVePoZGHLjGuPpAbHJ6OfDPHH/lGrywK4XfW//H2wd4imSTV0qAf3jtrqU2t5ATEUPgTpxrYj85s+BJcDFWquzCkb6aiPQ2RgGfnbaKpPF4ackbMtrES3z6iPcrcupE8L96Srvz1OS6iKpjcZmn1b5MWaZ6Wu2+zMApCgG74q4V1kITZifPMnGtlqE9uAlTwNSO9QC1KbKiytt9bT0y7G+IHHxeZsf4nhJ")
        self.assertEqual(k.title, "electra-3")
        k.delete()


class AuthenticatedUserOrganizations(TestCase):
    @Enterprise("zeus")
    def testGetOrgs(self):
        u = self.g.get_authenticated_user()
        orgs = u.get_orgs()
        self.assertEqual([o.login for o in orgs], ["olympus", "underground"])

    @Enterprise("zeus")
    def testGetOrgs_allParameters(self):
        u = self.g.get_authenticated_user()
        orgs = u.get_orgs(per_page=1)
        self.assertEqual([o.login for o in orgs], ["olympus", "underground"])

    @Enterprise("zeus")
    def testGetTeams(self):
        u = self.g.get_authenticated_user()
        teams = u.get_teams()
        self.assertEqual([t.name for t in teams], ["Owners", "Owners", "Gods"])

    @Enterprise("zeus")
    def testGetTeams_allParameters(self):
        u = self.g.get_authenticated_user()
        teams = u.get_teams(per_page=1)
        self.assertEqual([t.name for t in teams], ["Owners", "Owners", "Gods"])


class AuthenticatedUserRepositories(TestCase):
    @Enterprise("electra")
    def testGetRepo(self):
        u = self.g.get_authenticated_user()
        r = u.get_repo("immutable")
        self.assertEqual(r.full_name, "electra/immutable")

    @Enterprise("electra")
    def testGetRepos(self):
        u = self.g.get_authenticated_user()
        repos = u.get_repos()
        self.assertEqual([r.name for r in repos], ["contributors", "git-objects", "immutable", "issues", "issues", "mutable", "pulls"])

    @Enterprise("electra")
    def testGetRepos_allParameters(self):
        u = self.g.get_authenticated_user()
        repos = u.get_repos(type="public", sort="pushed", direction="asc", per_page=1)
        self.assertEqual([r.name for r in repos], ["pulls", "immutable", "contributors", "mutable", "issues", "git-objects"])

    @Enterprise("penelope")
    def testGetStarred(self):
        u = self.g.get_authenticated_user()
        repos = u.get_starred()
        self.assertEqual([r.full_name for r in repos], ["electra/mutable", "electra/immutable"])

    @Enterprise("penelope")
    def testGetStarred_allParameters(self):
        u = self.g.get_authenticated_user()
        repos = u.get_starred(sort="updated", direction="asc", per_page=1)
        self.assertEqual([r.full_name for r in repos], ["electra/immutable", "electra/mutable"])

    @Enterprise("penelope")
    def testAddToAndRemoveFromStarred(self):
        u = self.g.get_authenticated_user()
        self.assertTrue(u.has_in_starred(("electra", "mutable")))
        u.remove_from_starred(("electra", "mutable"))
        self.assertFalse(u.has_in_starred(("electra", "mutable")))
        u.add_to_starred(("electra", "mutable"))
        self.assertTrue(u.has_in_starred(("electra", "mutable")))

    @Enterprise("electra")
    def testCreateRepo(self):
        u = self.g.get_authenticated_user()
        r = u.create_repo("ephemeral")
        self.assertEqual(r.name, "ephemeral")
        self.assertIsNone(r.description)
        self.assertIsNone(r.homepage)
        self.assertEqual(r.private, False)
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        r.delete()

    @Enterprise("electra")
    def testCreateRepo_allParameters(self):
        u = self.g.get_authenticated_user()
        r = u.create_repo("ephemeral", description="Created by PyGithub", homepage="http://bar.com", private=True, has_issues=False, has_wiki=False, auto_init=True, gitignore_template="Python", license_template="mit")
        self.assertEqual(r.name, "ephemeral")
        self.assertEqual(r.description, "Created by PyGithub")
        self.assertEqual(r.homepage, "http://bar.com")
        self.assertEqual(r.private, True)
        self.assertEqual(r.has_issues, False)
        self.assertEqual(r.has_wiki, False)
        r.delete()

    @Enterprise("penelope")
    def testCreateFork(self):
        u = self.g.get_authenticated_user()
        r = u.create_fork(("electra", "mutable"))
        self.assertEqual(r.full_name, "penelope/mutable")
        r.delete()

    @Enterprise("electra")
    def testGetUserIssues(self):
        u = self.g.get_authenticated_user()
        issues = u.get_user_issues()
        self.assertEqual([i.title for i in issues[-3:]], ["Immutable issue"])

    @Enterprise("electra")
    def testGetUserIssues_allParameters(self):
        u = self.g.get_authenticated_user()
        issues = u.get_user_issues(filter="all", state="all", labels=["question", "enhancement"], sort="created", direction="desc", since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([i.title for i in issues[-3:]], ["Closed issue 1", "Closed issue 2", "Immutable issue"])

    @Enterprise("electra")
    def testGetIssues(self):
        u = self.g.get_authenticated_user()
        issues = u.get_issues()
        self.assertEqual([i.title for i in issues[-3:]], ["Immutable issue"])

    @Enterprise("electra")
    def testGetIssues_allParameters(self):
        u = self.g.get_authenticated_user()
        issues = u.get_issues(filter="all", state="all", labels=["question", "enhancement"], sort="created", direction="desc", since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([i.title for i in issues[-3:]], ["Closed issue 1", "Closed issue 2", "Immutable issue"])


class AuthenticatedUserSubscriptions(TestCase):
    @Enterprise("penelope")
    def testGetSubscriptions(self):
        u = self.g.get_authenticated_user()
        subs = u.get_subscriptions()
        self.assertEqual([r.full_name for r in subs], ["penelope/pulls", "electra/immutable", "penelope/immutable", "electra/mutable", "electra/issues", "penelope/mutable"])

    @Enterprise("penelope")
    def testGetSubscriptions_allParameters(self):
        u = self.g.get_authenticated_user()
        subs = u.get_subscriptions(per_page=1)
        self.assertEqual([r.full_name for r in subs], ["penelope/pulls", "electra/immutable", "penelope/immutable", "electra/mutable", "electra/issues", "penelope/mutable"])

    @Enterprise("penelope")
    def testGetSubscription(self):
        u = self.g.get_authenticated_user()
        s = u.get_subscription(("electra", "immutable"))
        self.assertEqual(s.repository_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable")

    @Enterprise("penelope")
    def testCreateSubscription(self):
        u = self.g.get_authenticated_user()
        s = u.create_subscription(("electra", "mutable"), subscribed=False, ignored=True)
        self.assertEqual(s.subscribed, False)
        self.assertEqual(s.ignored, True)
        s = u.create_subscription(("electra", "mutable"), subscribed=False, ignored=False)
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
