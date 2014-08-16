# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class AuthenticatedUserAttributes(TestCase):
    def testEnterpriseUser(self):
        u = self.antigone.get_authenticated_user()
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


class AuthenticatedUserAuthorizations(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        u = self.electra.get_authenticated_user()
        for a in u.get_authorizations():
            a.delete()
        a = u.create_authorization("a", scopes=["repo", "user"])
        u.create_authorization("b")
        return Data(id=a.id)

    def testGetAuthorization(self):
        u = self.electra.get_authenticated_user()
        a = u.get_authorization(self.data.id)
        self.assertEqual(a.note, "a")

    def testGetAuthorizations(self):
        u = self.electra.get_authenticated_user()
        auths = u.get_authorizations()
        self.assertEqual([a.note for a in auths], ["a", "b"])

    def testGetAuthorizations_allParameters(self):
        u = self.electra.get_authenticated_user()
        auths = u.get_authorizations(per_page=1)
        self.assertEqual([a.note for a in auths], ["a", "b"])

    def testCreateAuthorization(self):
        u = self.electra.get_authenticated_user()
        a = u.create_authorization("c")
        self.assertEqual(a.note, "c")
        self.assertEqual(a.scopes, [])
        self.assertEqual(a.note_url, None)
        self.assertEqual(a.app.client_id, "00000000000000000000")
        self.assertEqual(a.app.name, "c (API)")
        a.delete()

    def testCreateAuthorization_allParameters(self):
        u = self.electra.get_authenticated_user()
        a = u.create_authorization("d", scopes=["repo", "user"], note_url="http://foo.com", client_id="dfb1584c2c0674284875", client_secret="16a529070ec817d87e5b186d966fa935bfad1575")  # Create application manually as electra
        self.assertEqual(a.note, "d")
        self.assertEqual(a.scopes, ["repo", "user"])
        self.assertEqual(a.note_url, "http://foo.com")
        self.assertEqual(a.app.client_id, "dfb1584c2c0674284875")
        self.assertEqual(a.app.name, "authorizations")
        a.delete()

    def testGetOrCreateAuthorization(self):
        u = self.electra.get_authenticated_user()
        a = u.get_or_create_authorization("dfb1584c2c0674284875", "16a529070ec817d87e5b186d966fa935bfad1575")  # Create application manually as electra
        self.assertEqual(a.note, None)
        self.assertEqual(a.scopes, [])
        self.assertEqual(a.note_url, None)
        self.assertEqual(a.app.client_id, "dfb1584c2c0674284875")
        self.assertEqual(a.app.name, "authorizations")
        a.delete()

    def testGetOrCreateAuthorization_allParameters(self):
        u = self.electra.get_authenticated_user()
        a = u.get_or_create_authorization("dfb1584c2c0674284875", "16a529070ec817d87e5b186d966fa935bfad1575", scopes=["repo", "user"], note="e", note_url="http://foo.com")  # Create application manually as electra
        self.assertEqual(a.note, "e")
        self.assertEqual(a.scopes, ["repo", "user"])
        self.assertEqual(a.note_url, "http://foo.com")
        self.assertEqual(a.app.client_id, "dfb1584c2c0674284875")
        self.assertEqual(a.app.name, "authorizations")
        a.delete()


class AuthenticatedUserEdit(TestCase):
    def testName(self):
        u = self.penelope.get_authenticated_user()
        self.assertEqual(u.name, None)
        u.edit(name="Penelope")
        self.assertEqual(u.name, "Penelope")
        u.edit(name=PyGithub.Blocking.Reset)
        self.assertEqual(u.name, None)

    def testEmail(self):
        u = self.penelope.get_authenticated_user()
        self.assertEqual(u.email, None)
        u.edit(email="ghe-penelope@jacquev6.net")
        self.assertEqual(u.email, "ghe-penelope@jacquev6.net")
        u.edit(email=PyGithub.Blocking.Reset)
        self.assertEqual(u.email, None)

    def testBlog(self):
        u = self.penelope.get_authenticated_user()
        self.assertEqual(u.blog, None)
        u.edit(blog="http://jacquev6.net/penelope")
        self.assertEqual(u.blog, "http://jacquev6.net/penelope")
        u.edit(blog=PyGithub.Blocking.Reset)
        self.assertEqual(u.blog, None)

    def testCompany(self):
        u = self.penelope.get_authenticated_user()
        self.assertEqual(u.company, None)
        u.edit(company="Penelope Software")
        self.assertEqual(u.company, "Penelope Software")
        u.edit(company=PyGithub.Blocking.Reset)
        self.assertIsNone(u.company)

    def testLocation(self):
        u = self.penelope.get_authenticated_user()
        self.assertEqual(u.location, None)
        u.edit(location="Greece")
        self.assertEqual(u.location, "Greece")
        u.edit(location=PyGithub.Blocking.Reset)
        self.assertEqual(u.location, None)

    def testHireable(self):
        u = self.penelope.get_authenticated_user()
        self.assertEqual(u.hireable, False)
        u.edit(hireable=PyGithub.Blocking.Reset)
        self.assertIsNone(u.hireable)
        u.edit(hireable=False)
        self.assertEqual(u.hireable, False)


class AuthenticatedUserEmails(TestCase):
    def testGetEmails(self):
        u = self.penelope.get_authenticated_user()
        emails = u.get_emails()
        self.assertEqual(len(emails), 1)
        self.assertEqual(emails[0].email, "ghe-penelope@jacquev6.net")
        self.assertEqual(emails[0].primary, True)
        self.assertEqual(emails[0].verified, False)

    def testAddOneToAndRemoveOneFromEmails(self):
        u = self.penelope.get_authenticated_user()
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net"])
        u.add_to_emails("foo@bar.com")
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net", "foo@bar.com"])
        u.remove_from_emails("foo@bar.com")
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net"])

    def testAddSeveralToAndRemoveSeveralFromEmails(self):
        u = self.penelope.get_authenticated_user()
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net"])
        u.add_to_emails("foo@bar.com", "baz@42.com")
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net", "foo@bar.com", "baz@42.com"])
        u.remove_from_emails("foo@bar.com", "baz@42.com")
        self.assertEqual([e.email for e in u.get_emails()], ["ghe-penelope@jacquev6.net"])


class AuthenticatedUserFollowing(TestCase):
    def testGetFollowing(self):
        u = self.electra.get_authenticated_user()
        following = u.get_following()
        self.assertEqual([f.login for f in following], ["zeus", "poseidon"])

    def testGetFollowing_allParameters(self):
        u = self.electra.get_authenticated_user()
        following = u.get_following(per_page=1)
        self.assertEqual([f.login for f in following], ["zeus", "poseidon"])

    def testAddToAndRemoveFromFollowing(self):
        u = self.penelope.get_authenticated_user()
        self.assertFalse(u.has_in_following("zeus"))
        u.add_to_following("zeus")
        self.assertTrue(u.has_in_following("zeus"))
        u.remove_from_following("zeus")
        self.assertFalse(u.has_in_following("zeus"))

    def testGetFollowers(self):
        u = self.zeus.get_authenticated_user()
        followers = u.get_followers()
        self.assertEqual([f.login for f in followers], ["electra", "poseidon"])

    def testGetFollowers_allParameters(self):
        u = self.zeus.get_authenticated_user()
        followers = u.get_followers(per_page=1)
        self.assertEqual([f.login for f in followers], ["electra", "poseidon"])


class AuthenticatedUserGists(TestCase):
    mutableGistId = "8204fee2d7e3f12bde22"

    def testGetGists(self):
        u = self.electra.get_authenticated_user()
        gists = u.get_gists()
        self.assertEqual([g.description for g in gists], ["Mutable gist 2", "Mutable gist 1", "Immutable gist"])

    def testGetGists_allParameters(self):
        u = self.electra.get_authenticated_user()
        gists = u.get_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([g.description for g in gists], ["Mutable gist 2", "Mutable gist 1", "Immutable gist"])

    def testGetStarredGists(self):
        u = self.penelope.get_authenticated_user()
        gists = u.get_starred_gists()
        self.assertEqual([g.description for g in gists], ["Mutable gist 1", "Immutable gist"])

    def testGetStarredGists_allParameters(self):
        u = self.penelope.get_authenticated_user()
        gists = u.get_starred_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([g.description for g in gists], ["Mutable gist 1", "Immutable gist"])

    def testAddToAndRemoveFromStarredGists(self):
        u = self.penelope.get_authenticated_user()
        self.assertFalse(u.has_in_starred_gists(self.mutableGistId))
        u.add_to_starred_gists(self.mutableGistId)
        self.assertTrue(u.has_in_starred_gists(self.mutableGistId))
        u.remove_from_starred_gists(self.mutableGistId)
        self.assertFalse(u.has_in_starred_gists(self.mutableGistId))

    def testCreateGistFork(self):
        u = self.penelope.get_authenticated_user()
        g = u.create_gist_fork(self.mutableGistId)
        self.assertEqual(g.description, "Mutable gist 2")
        self.assertEqual(g.owner.login, "penelope")
        g.delete()

    def testCreateGist(self):
        # @todoAlpha Create input class for files
        u = self.electra.get_authenticated_user()
        g = u.create_gist(files={"foo.txt": {"content": "barbaz"}})
        self.assertIsNone(g.description)
        self.assertEqual(g.public, False)
        g.delete()

    def testCreateGist_allParameters(self):
        u = self.electra.get_authenticated_user()
        g = u.create_gist(files={"foo.txt": {"content": "barbaz"}, "bar.txt": {"content": "tartempion"}}, public=True, description="Gist created by PyGithub")
        self.assertEqual(g.description, "Gist created by PyGithub")
        self.assertEqual(g.public, True)
        g.delete()


class AuthenticatedUserKeys(TestCase):
    def testGetKeys(self):
        u = self.electra.get_authenticated_user()
        keys = u.get_keys()
        self.assertEqual([k.title for k in keys], ["electra-1", "electra-2"])

    def testGetKey(self):
        u = self.electra.get_authenticated_user()
        k = u.get_key(4)
        self.assertEqual(k.title, "electra-1")

    def testCreateKey(self):
        u = self.electra.get_authenticated_user()
        k = u.create_key("electra-3", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCh/ih0dj35ZIrOSrYIih0ulcIP48H4DMtgLPUfX0BHuknkf9sCtAM+lURjHVsiZNn4mJDQwH0gHZ+NbisN7yKexArffuemvjFVSALlnYXW78SagsrEvAlVePoZGHLjGuPpAbHJ6OfDPHH/lGrywK4XfW//H2wd4imSTV0qAf3jtrqU2t5ATEUPgTpxrYj85s+BJcDFWquzCkb6aiPQ2RgGfnbaKpPF4ackbMtrES3z6iPcrcupE8L96Srvz1OS6iKpjcZmn1b5MWaZ6Wu2+zMApCgG74q4V1kITZifPMnGtlqE9uAlTwNSO9QC1KbKiytt9bT0y7G+IHHxeZsf4nhJ")
        self.assertEqual(k.title, "electra-3")
        k.delete()


class AuthenticatedUserOrganizations(TestCase):
    def testGetOrgs(self):
        u = self.zeus.get_authenticated_user()
        orgs = u.get_orgs()
        self.assertEqual([o.login for o in orgs], ["olympus", "underground"])

    def testGetOrgs_allParameters(self):
        u = self.zeus.get_authenticated_user()
        orgs = u.get_orgs(per_page=1)
        self.assertEqual([o.login for o in orgs], ["olympus", "underground"])

    def testGetTeams(self):
        u = self.zeus.get_authenticated_user()
        teams = u.get_teams()
        self.assertEqual([t.name for t in teams], ["Owners", "Owners", "Gods"])

    def testGetTeams_allParameters(self):
        u = self.zeus.get_authenticated_user()
        teams = u.get_teams(per_page=1)
        self.assertEqual([t.name for t in teams], ["Owners", "Owners", "Gods"])


class AuthenticatedUserRepositories(TestCase):
    def testGetRepo(self):
        u = self.electra.get_authenticated_user()
        r = u.get_repo("immutable")
        self.assertEqual(r.full_name, "electra/immutable")

    def testGetRepos(self):
        u = self.electra.get_authenticated_user()
        repos = u.get_repos()
        self.assertEqual([r.name for r in repos], ["contributors", "git-objects", "immutable", "issues", "issues", "mutable", "pulls"])

    def testGetRepos_allParameters(self):
        u = self.electra.get_authenticated_user()
        repos = u.get_repos(type="public", sort="pushed", direction="asc", per_page=1)
        self.assertEqual([r.name for r in repos], ["pulls", "immutable", "contributors", "mutable", "issues", "git-objects"])

    def testGetStarred(self):
        u = self.penelope.get_authenticated_user()
        repos = u.get_starred()
        self.assertEqual([r.full_name for r in repos], ["electra/mutable", "electra/immutable"])

    def testGetStarred_allParameters(self):
        u = self.penelope.get_authenticated_user()
        repos = u.get_starred(sort="updated", direction="asc", per_page=1)
        self.assertEqual([r.full_name for r in repos], ["electra/immutable", "electra/mutable"])

    def testAddToAndRemoveFromStarred(self):
        u = self.penelope.get_authenticated_user()
        self.assertTrue(u.has_in_starred(("electra", "mutable")))
        u.remove_from_starred(("electra", "mutable"))
        self.assertFalse(u.has_in_starred(("electra", "mutable")))
        u.add_to_starred(("electra", "mutable"))
        self.assertTrue(u.has_in_starred(("electra", "mutable")))

    def testCreateRepo(self):
        u = self.electra.get_authenticated_user()
        r = u.create_repo("ephemeral")
        self.assertEqual(r.name, "ephemeral")
        self.assertIsNone(r.description)
        self.assertIsNone(r.homepage)
        self.assertEqual(r.private, False)
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        r.delete()

    def testCreateRepo_allParameters(self):
        u = self.electra.get_authenticated_user()
        r = u.create_repo("ephemeral", description="Created by PyGithub", homepage="http://bar.com", private=True, has_issues=False, has_wiki=False, auto_init=True, gitignore_template="Python", license_template="mit")
        self.assertEqual(r.name, "ephemeral")
        self.assertEqual(r.description, "Created by PyGithub")
        self.assertEqual(r.homepage, "http://bar.com")
        self.assertEqual(r.private, True)
        self.assertEqual(r.has_issues, False)
        self.assertEqual(r.has_wiki, False)
        r.delete()

    def testCreateFork(self):
        u = self.penelope.get_authenticated_user()
        r = u.create_fork(("electra", "mutable"))
        self.assertEqual(r.full_name, "penelope/mutable")
        r.delete()

    def testGetUserIssues(self):
        u = self.electra.get_authenticated_user()
        issues = u.get_user_issues()
        self.assertEqual([i.title for i in issues[-3:]], ["Immutable issue"])

    def testGetUserIssues_allParameters(self):
        u = self.electra.get_authenticated_user()
        issues = u.get_user_issues(filter="all", state="all", labels=["question", "enhancement"], sort="created", direction="desc", since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([i.title for i in issues[-3:]], ["Closed issue 1", "Closed issue 2", "Immutable issue"])

    def testGetIssues(self):
        u = self.electra.get_authenticated_user()
        issues = u.get_issues()
        self.assertEqual([i.title for i in issues[-3:]], ["Immutable issue"])

    def testGetIssues_allParameters(self):
        u = self.electra.get_authenticated_user()
        issues = u.get_issues(filter="all", state="all", labels=["question", "enhancement"], sort="created", direction="desc", since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([i.title for i in issues[-3:]], ["Closed issue 1", "Closed issue 2", "Immutable issue"])


class AuthenticatedUserSubscriptions(TestCase):
    def testGetSubscriptions(self):
        u = self.penelope.get_authenticated_user()
        subs = u.get_subscriptions()
        self.assertEqual([r.full_name for r in subs], ["penelope/pulls", "electra/immutable", "penelope/immutable", "electra/mutable", "electra/issues", "penelope/mutable"])

    def testGetSubscriptions_allParameters(self):
        u = self.penelope.get_authenticated_user()
        subs = u.get_subscriptions(per_page=1)
        self.assertEqual([r.full_name for r in subs], ["penelope/pulls", "electra/immutable", "penelope/immutable", "electra/mutable", "electra/issues", "penelope/mutable"])

    def testGetSubscription(self):
        u = self.penelope.get_authenticated_user()
        s = u.get_subscription(("electra", "immutable"))
        self.assertEqual(s.repository_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable")

    def testCreateSubscription(self):
        u = self.penelope.get_authenticated_user()
        s = u.create_subscription(("electra", "mutable"), subscribed=False, ignored=True)
        self.assertEqual(s.subscribed, False)
        self.assertEqual(s.ignored, True)
        s = u.create_subscription(("electra", "mutable"), subscribed=False, ignored=False)
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
