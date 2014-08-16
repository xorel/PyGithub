# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class RepositoryAttributes(TestCase):
    def testOwned(self):
        r = self.electra.get_repo(("electra", "immutable"))
        self.assertEqual(r.archive_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/{archive_format}{/ref}")
        self.assertEqual(r.assignees_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/assignees{/user}")
        self.assertEqual(r.blobs_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/blobs{/sha}")
        self.assertEqual(r.branches_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/branches{/branch}")
        self.assertEqual(r.clone_url, "http://github.home.jacquev6.net/electra/immutable.git")
        self.assertEqual(r.collaborators_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/collaborators{/collaborator}")
        self.assertEqual(r.comments_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/comments{/number}")
        self.assertEqual(r.commits_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/commits{/sha}")
        self.assertEqual(r.compare_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/compare/{base}...{head}")
        self.assertEqual(r.contents_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/contents/{+path}")
        self.assertEqual(r.contributors_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/contributors")
        self.assertEqual(r.created_at, datetime.datetime(2014, 8, 4, 2, 5, 7))
        self.assertEqual(r.default_branch, "master")
        self.assertEqual(r.description, None)
        self.assertEqual(r.downloads_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/downloads")
        self.assertEqual(r.events_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/events")
        self.assertEqual(r.fork, False)
        self.assertEqual(r.forks_count, 2)
        self.assertEqual(r.forks_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/forks")
        self.assertEqual(r.full_name, "electra/immutable")
        self.assertEqual(r.git_commits_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/commits{/sha}")
        self.assertEqual(r.git_refs_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/refs{/sha}")
        self.assertEqual(r.git_tags_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/tags{/sha}")
        self.assertEqual(r.git_url, "git://github.home.jacquev6.net/electra/immutable.git")
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        self.assertEqual(r.homepage, None)
        self.assertEqual(r.hooks_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/hooks")
        self.assertEqual(r.html_url, "http://github.home.jacquev6.net/electra/immutable")
        self.assertEqual(r.id, 34)
        self.assertEqual(r.issue_comment_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/issues/comments/{number}")
        self.assertEqual(r.issue_events_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/issues/events{/number}")
        self.assertEqual(r.issues_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/issues{/number}")
        self.assertEqual(r.keys_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/keys{/key_id}")
        self.assertEqual(r.labels_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/labels{/name}")
        self.assertEqual(r.language, None)
        self.assertEqual(r.languages_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/languages")
        self.assertEqual(r.merges_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/merges")
        self.assertEqual(r.milestones_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/milestones{/number}")
        self.assertEqual(r.mirror_url, None)
        self.assertEqual(r.name, "immutable")
        self.assertEqual(r.network_count, 2)
        self.assertEqual(r.notifications_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/notifications{?since,all,participating}")
        self.assertEqual(r.open_issues_count, 0)
        self.assertEqual(r.owner.login, "electra")
        self.assertEqual(r.parent, None)
        self.assertEqual(r.permissions.admin, True)
        self.assertEqual(r.permissions.pull, True)
        self.assertEqual(r.permissions.push, True)
        self.assertEqual(r.private, False)
        self.assertEqual(r.pulls_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/pulls{/number}")
        self.assertEqual(r.pushed_at, datetime.datetime(2014, 8, 4, 2, 5, 9))
        self.assertEqual(r.releases_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/releases{/id}")
        self.assertEqual(r.size, 0)
        self.assertEqual(r.source, None)
        self.assertEqual(r.ssh_url, "git@github.home.jacquev6.net:electra/immutable.git")
        self.assertEqual(r.stargazers_count, 0)
        self.assertEqual(r.stargazers_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/stargazers")
        self.assertEqual(r.statuses_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/statuses/{sha}")
        self.assertEqual(r.subscribers_count, 1)
        self.assertEqual(r.subscribers_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/subscribers")
        self.assertEqual(r.subscription_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/subscription")
        self.assertEqual(r.svn_url, "http://github.home.jacquev6.net/electra/immutable")
        self.assertEqual(r.tags_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/tags")
        self.assertEqual(r.teams_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/teams")
        self.assertEqual(r.trees_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/trees{/sha}")
        self.assertEqual(r.updated_at, datetime.datetime(2014, 8, 4, 2, 5, 9))
        self.assertEqual(r.url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable")
        self.assertEqual(r.watchers_count, 0)
        self.assertIsInstance(r.owner, PyGithub.Blocking.User.User)

    def testForkByOrg(self):
        r = self.electra.get_repo(("olympus", "immutable"))
        self.assertEqual(r.fork, True)
        self.assertEqual(r.parent.owner.login, "electra")
        self.assertEqual(r.source.owner.login, "electra")
        self.assertIsInstance(r.owner, PyGithub.Blocking.Organization.Organization)
        self.assertIsInstance(r.parent.owner, PyGithub.Blocking.User.User)
        self.assertIsInstance(r.source.owner, PyGithub.Blocking.User.User)

    def testForkOfFork(self):
        r = self.electra.get_repo(("penelope", "immutable"))
        self.assertEqual(r.parent.owner.login, "olympus")
        self.assertEqual(r.source.owner.login, "electra")
        self.assertIsInstance(r.owner, PyGithub.Blocking.User.User)
        self.assertIsInstance(r.parent.owner, PyGithub.Blocking.Organization.Organization)
        self.assertIsInstance(r.source.owner, PyGithub.Blocking.User.User)


class RepositoryContents(TestCase):
    # @todoAlpha Allow methods in inner structs: Repository.Dir needs get_contents
    #   methods:
    # - name: get_contents
    #   end_point: GET /repos/:owner/:repo/contents/:path
    #   url_template: attribute url
    #   return_type:
    #     container: list
    #     content:
    #       union: [File, Dir, Submodule, SymLink]
    # @todoAlpha We could also have a Dir.create_file method

    def testGetRootContents(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_contents("")
        self.assertIsInstance(c[0], PyGithub.Blocking.File.File)
        self.assertEqual(c[0].path, "README.md")
        self.assertIsInstance(c[1], PyGithub.Blocking.File.File)
        self.assertEqual(c[1].path, "foo.md")

    def testGetRootContents_allParameters(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_contents("", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertIsInstance(c[0], PyGithub.Blocking.File.File)
        self.assertEqual(c[0].path, "a_blob")
        self.assertIsInstance(c[1], PyGithub.Blocking.Submodule.Submodule)
        self.assertEqual(c[1].path, "a_submodule")
        self.assertIsInstance(c[2], PyGithub.Blocking.SymLink.SymLink)
        self.assertEqual(c[2].path, "a_symlink")
        self.assertIsInstance(c[3], PyGithub.Blocking.Repository.Repository.Dir)
        self.assertEqual(c[3].git_url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/git/trees/65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(c[3].html_url, "http://github.home.jacquev6.net/electra/git-objects/tree/db09e03a13f7910b9cae93ca91cd35800e15c695/a_tree")
        self.assertEqual(c[3].name, "a_tree")
        self.assertEqual(c[3].path, "a_tree")
        self.assertEqual(c[3].sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(c[3].size, 0)
        self.assertEqual(c[3].type, "dir")
        self.assertEqual(c[3].url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/contents/a_tree?ref=db09e03a13f7910b9cae93ca91cd35800e15c695")  # Dir is not updatable because its url points to a list of its contents, not its hash representation

    def testGetDirContents(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_contents("a_tree", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertIsInstance(c[0], PyGithub.Blocking.File.File)

    def testGetFileContents(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_contents("a_blob", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertIsInstance(c, PyGithub.Blocking.File.File)

    def testGetFileInDirContents(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_contents("a_tree/test.txt", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertIsInstance(c, PyGithub.Blocking.File.File)

    def testGetSubmoduleContents(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_contents("a_submodule", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertIsInstance(c, PyGithub.Blocking.Submodule.Submodule)

    def testGetSymlinkContents(self):
        c = self.electra.get_repo(("electra", "git-objects")).get_contents("a_symlink", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertIsInstance(c, PyGithub.Blocking.SymLink.SymLink)

    def testGetReadme(self):
        c = self.electra.get_repo(("electra", "immutable")).get_readme()
        self.assertIsInstance(c, PyGithub.Blocking.File.File)
        self.assertEqual(c.path, "README.md")

    def testGetReadme_allParameters(self):
        c = self.electra.get_repo(("electra", "immutable")).get_readme(ref="master")
        self.assertIsInstance(c, PyGithub.Blocking.File.File)
        self.assertEqual(c.path, "README.md")

    def testCreateFile(self):
        repo = self.electra.get_repo(("electra", "git-objects"))
        cc = repo.create_file("foo.txt", "Add foo.txt", "Q3JlYXRlZCBieSBQeUdpdGh1Yg==")
        self.assertEqual(cc.commit.message, "Add foo.txt")
        self.assertEqual(cc.content.path, "foo.txt")
        repo.get_git_ref("refs/heads/master").edit("627777afd4859d16e30880f4d8d0a178d99d395c", force=True)

    def testCreateFile_allParameters(self):
        repo = self.electra.get_repo(("electra", "git-objects"))
        ref = repo.create_git_ref("refs/heads/ephemeral", "627777afd4859d16e30880f4d8d0a178d99d395c")
        cc = repo.create_file("foo.txt", "Add foo.txt", "Q3JlYXRlZCBieSBQeUdpdGh1Yg==", branch="ephemeral", author={"name": "John Doe", "email": "john@doe.com"}, committer={"name": "Jane Doe", "email": "jane@doe.com"})
        self.assertEqual(cc.commit.author.name, "John Doe")
        self.assertEqual(cc.commit.committer.name, "Jane Doe")
        self.assertEqual(cc.content.url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/contents/foo.txt?ref=ephemeral")
        ref.delete()


class RepositoryDelete(TestCase):
    def test(self):
        r = self.electra.get_authenticated_user().create_repo("ephemeral")
        r.delete()


class RepositoryEdit(TestCase):
    def setUpEnterprise(self):
        electra = self.electra.get_authenticated_user()
        try:
            electra.get_repo("edit").delete()
        except PyGithub.ObjectNotFoundException:  # pragma no cover (setup branch)
            pass  # pragma no cover (setup branch)
        r = electra.create_repo("edit", auto_init=True)
        r.create_git_ref("refs/heads/develop", r.get_git_ref("refs/heads/master").object.sha)

    def testName(self):
        r = self.electra.get_repo(("electra", "edit"))
        self.assertEqual(r.name, "edit")
        r.edit(name="edit-bis")
        self.assertEqual(r.name, "edit-bis")
        r.edit(name="edit")
        self.assertEqual(r.name, "edit")

    def testDescription(self):
        r = self.electra.get_repo(("electra", "edit"))
        self.assertEqual(r.description, None)
        r.edit(description="Mutable repository")
        self.assertEqual(r.description, "Mutable repository")
        r.edit(description=PyGithub.Blocking.Reset)
        self.assertEqual(r.description, None)

    def testHomepage(self):
        r = self.electra.get_repo(("electra", "edit"))
        self.assertEqual(r.homepage, None)
        r.edit(homepage="http://foo.com")
        self.assertEqual(r.homepage, "http://foo.com")
        r.edit(homepage=PyGithub.Blocking.Reset)
        self.assertEqual(r.homepage, None)

    def testPrivate(self):
        r = self.electra.get_repo(("electra", "edit"))
        self.assertEqual(r.private, False)
        r.edit(private=True)
        self.assertEqual(r.private, True)
        r.edit(private=False)
        self.assertEqual(r.private, False)

    def testHasIssues(self):
        r = self.electra.get_repo(("electra", "edit"))
        self.assertEqual(r.has_issues, True)
        r.edit(has_issues=False)
        self.assertEqual(r.has_issues, False)
        r.edit(has_issues=True)
        self.assertEqual(r.has_issues, True)

    def testHasWiki(self):
        r = self.electra.get_repo(("electra", "edit"))
        self.assertEqual(r.has_wiki, True)
        r.edit(has_wiki=False)
        self.assertEqual(r.has_wiki, False)
        r.edit(has_wiki=True)
        self.assertEqual(r.has_wiki, True)

    def testDefaultBranch(self):
        r = self.electra.get_repo(("electra", "edit"))
        self.assertEqual(r.default_branch, "master")
        r.edit(default_branch="develop")
        self.assertEqual(r.default_branch, "develop")
        r.edit(default_branch="master")
        self.assertEqual(r.default_branch, "master")


class RepositoryGitStuff(TestCase):
    def testGetBranches(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        branches = r.get_branches()
        self.assertEqual([b.name for b in branches], ["develop", "master"])

    def testGetBranches_allParameters(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        branches = r.get_branches(per_page=1)
        self.assertEqual([b.name for b in branches], ["develop", "master"])

    def testGetBranch(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        b = r.get_branch("develop")
        self.assertEqual(b.commit.author.login, "electra")

    # @todoSomeday Consider opening an issue to GitHub to fix inconsistency with Branch:
    # Branch.update can be tested like this if Branch is modified to take its url attribute from _links["self"]
    # but _links is returned only by Repository.get_branch, not by Repository.get_branches
    # so we have no way to make Branch generaly updatable
    # def testUpdateBranch(self):
    #     r = self.electra.get_repo(("electra", "git-objects"))
    #     b = r.get_branch("test_update")
    #     self.assertEqual(b.commit.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
    #     self.assertFalse(b.update())
    #     self.assertEqual(b.commit.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
    #     r.get_git_ref("refs/heads/test_update").edit(sha="7820fadc2429652016611e98fdc21766ba075161")
    #     self.assertTrue(b.update())
    #     self.assertEqual(b.commit.sha, "7820fadc2429652016611e98fdc21766ba075161")
    #     r.get_git_ref("refs/heads/test_update").edit(sha="e078f69fb050b75fe5f3c7aa70adc24d692e75b8", force=True)

    def testGetCommits(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        commits = r.get_commits()
        self.assertEqual([c.commit.message for c in commits], ["Modify README.md", "Create foo.md", "Initial commit"])

    def testGetCommits_allParameters(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        commits = r.get_commits(sha="refs/heads/master", path="README.md", author="electra", since=datetime.datetime(2014, 1, 1, 0, 0, 0), until=datetime.datetime(2049, 12, 31, 23, 59, 59), per_page=1)
        self.assertEqual([c.commit.message for c in commits], ["Modify README.md", "Initial commit"])

    def testGetCommit(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        c = r.get_commit("refs/heads/master")
        self.assertEqual(c.commit.message, "Modify README.md")

    def testGetTags(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tags = r.get_tags()
        self.assertEqual([t.name for t in tags], ["light-tag-2", "light-tag-1"])
        self.assertEqual(tags[0].commit.sha, "d9343bbb63ef53a264dee9ccbd75c6b5ebae0bef")
        self.assertEqual(tags[0].tarball_url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/tarball/light-tag-2")
        self.assertEqual(tags[0].zipball_url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/zipball/light-tag-2")

    def testGetTags_allParameters(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tags = r.get_tags(per_page=1)
        self.assertEqual([t.name for t in tags], ["light-tag-2", "light-tag-1"])

    def testGetGitTag(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        t = r.get_git_tag("b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        self.assertEqual(t.tag, "heavy-tag")

    def testGetGitRefs(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        refs = r.get_git_refs()
        # @todoAlpha What about GET /repos/.../git/refs/heads? It returns a list of refs as well
        self.assertEqual([r.ref for r in refs], ["refs/heads/develop", "refs/heads/master", "refs/tags/light-tag-1", "refs/tags/light-tag-2"])

    def testGetGitRefs_allParameters(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        refs = r.get_git_refs(per_page=2)
        self.assertEqual([r.ref for r in refs], ["refs/heads/develop", "refs/heads/master", "refs/tags/light-tag-1", "refs/tags/light-tag-2"])

    def testGetGitRef(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        ref = r.get_git_ref("refs/heads/develop")
        # @todoAlpha Test get_git_ref with a string not starting with "refs/"
        self.assertEqual(ref.ref, "refs/heads/develop")

    def testCreateGitBlob(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        blob = r.create_git_blob("This is some content", "utf8")
        self.assertEqual(blob.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")

    def testGetGitBlob(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        blob = r.get_git_blob("3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(blob.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")

    def testCreateGitTree(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tree = r.create_git_tree(tree=[{"path": "test.txt", "mode": "100644", "type": "blob", "sha": "3daf0da6bca38181ab52610dd6af6e92f1a5469d"}])
        self.assertEqual(tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")

    def testGetGitTree(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tree = r.get_git_tree("65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(len(tree.tree), 1)

    def testGetGitCommit(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        commit = r.get_git_commit("f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(commit.message, "first commit")

    def testCreateInitialGitCommit(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[])
        self.assertEqual(commit.message, "first commit")
        self.assertEqual(commit.tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(len(commit.parents), 0)

    def testCreateInitialGitCommit_allParameters(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[], author={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"}, committer={"name": "Jane Doe", "email": "jane@doe.com", "date": "2000-01-01T00:00:00Z"})
        self.assertEqual(commit.author.name, "John Doe")
        self.assertEqual(commit.author.email, "john@doe.com")
        self.assertEqual(commit.author.date, datetime.datetime(1999, 12, 31, 23, 59, 59))
        self.assertEqual(commit.committer.name, "Jane Doe")
        self.assertEqual(commit.committer.email, "jane@doe.com")
        self.assertEqual(commit.committer.date, datetime.datetime(2000, 1, 1, 0, 0, 0))
        self.assertEqual(commit.sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")

    def testCreateSubsequentGitCommit(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="second commit", parents=["f739e7ae2fd0e7b2bce99c073bcc7b57d713877e"])
        self.assertEqual(commit.parents[0].sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")

    def testCreateGitRef_commit(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        ref = r.create_git_ref(ref="refs/tests/commit_ref", sha="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(ref.ref, "refs/tests/commit_ref")
        self.assertEqual(ref.object.type, "commit")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitCommit.GitCommit)
        ref.delete()

    def testCreateGitRef_tree(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        ref = r.create_git_ref(ref="refs/tests/tree_ref", sha="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(ref.ref, "refs/tests/tree_ref")
        self.assertEqual(ref.object.type, "tree")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitTree.GitTree)
        ref.delete()

    def testCreateGitRef_blob(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        ref = r.create_git_ref(ref="refs/tests/blob_ref", sha="3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(ref.ref, "refs/tests/blob_ref")
        self.assertEqual(ref.object.type, "blob")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitBlob.GitBlob)
        ref.delete()

    def testCreateGitRef_tag(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        ref = r.create_git_ref(ref="refs/tests/tag_ref", sha="b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        self.assertEqual(ref.ref, "refs/tests/tag_ref")
        self.assertEqual(ref.object.type, "tag")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitTag.GitTag)
        ref.delete()

    def testCreateGitRef_existing(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.create_git_ref(ref="refs/heads/master", sha="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")

    def testCreateGitTag_allParameters(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="heavy-tag", message="This is a tag", object="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e", type="commit", tagger={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"})
        self.assertEqual(tag.tagger.name, "John Doe")
        self.assertEqual(tag.tagger.email, "john@doe.com")
        self.assertEqual(tag.tagger.date, datetime.datetime(1999, 12, 31, 23, 59, 59))
        self.assertEqual(tag.sha, "b55a47efb4f8c891b6719a3d85a80c7f875e33ec")

    def testCreateGitTag_commit(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="commit_tag", message="This is a commit tag", object="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e", type="commit")
        self.assertEqual(tag.object.type, "commit")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitCommit.GitCommit)

    def testCreateGitTag_tree(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="tree_tag", message="This is a tree tag", object="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", type="tree")
        self.assertEqual(tag.object.type, "tree")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitTree.GitTree)

    def testCreateGitTag_blob(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="blob_tag", message="This is a blob tag", object="3daf0da6bca38181ab52610dd6af6e92f1a5469d", type="blob")
        self.assertEqual(tag.object.type, "blob")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitBlob.GitBlob)

    def testCreateGitTag_tag(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="tag_tag", message="This is a tag tag", object="b55a47efb4f8c891b6719a3d85a80c7f875e33ec", type="tag")
        self.assertEqual(tag.object.type, "tag")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitTag.GitTag)

    def testCreateGitTag_badType(self):
        r = self.electra.get_repo(("electra", "git-objects"))
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.create_git_tag(tag="bad_tag", message="This is a tag to a commit, pretending to be a blob", object="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e", type="blob")


class RepositoryIssues(TestCase):
    def testCreateIssue(self):
        r = self.electra.get_repo(("electra", "mutable"))
        issue = r.create_issue("Created by PyGithub")
        self.assertEqual(issue.title, "Created by PyGithub")
        self.assertIsNone(issue.body)
        self.assertIsNone(issue.assignee)
        self.assertIsNone(issue.milestone)
        self.assertEqual(len(issue.labels), 0)
        issue.edit(state="closed")

    def testCreateIssue_allParameters(self):
        r = self.electra.get_repo(("electra", "mutable"))
        issue = r.create_issue("Also created by PyGithub", body="Body", assignee="electra", milestone=1, labels=["question"])
        self.assertEqual(issue.title, "Also created by PyGithub")
        self.assertEqual(issue.body, "Body")
        self.assertEqual(issue.assignee.login, "electra")
        self.assertEqual(issue.milestone.number, 1)
        self.assertEqual(len(issue.labels), 1)
        issue.edit(state="closed")

    def testGetIssue(self):
        r = self.electra.get_repo(("electra", "issues"))
        issue = r.get_issue(1)
        self.assertEqual(issue.title, "Immutable issue")

    def testGetIssues(self):
        r = self.electra.get_repo(("electra", "issues"))
        issues = r.get_issues()
        self.assertEqual([i.title for i in issues], ["Mutable issue", "Immutable issue"])

    def testGetIssues_allParameters(self):
        r = self.electra.get_repo(("electra", "issues"))
        issues = r.get_issues(milestone=1, state="closed", assignee="electra", creator="penelope", mentioned="electra", labels=["question"], sort="created", direction="asc", since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([i.title for i in issues], ["Closed issue 1", "Closed issue 2"])

    def testHasInAssignees(self):
        r = self.electra.get_repo(("electra", "issues"))
        self.assertTrue(r.has_in_assignees("penelope"))
        self.assertFalse(r.has_in_assignees("zeus"))

    def testGetAssignees(self):
        r = self.electra.get_repo(("electra", "issues"))
        assignees = r.get_assignees()
        self.assertEqual([a.login for a in assignees], ["electra", "penelope"])

    def testGetAssignees_allParameters(self):
        r = self.electra.get_repo(("electra", "issues"))
        assignees = r.get_assignees(per_page=1)
        self.assertEqual([a.login for a in assignees], ["electra", "penelope"])

    def testGetLabels(self):
        r = self.electra.get_repo(("electra", "issues"))
        labels = r.get_labels()
        self.assertEqual([l.name for l in labels], ["bug", "duplicate", "enhancement", "help wanted", "invalid", "question", "wontfix"])

    def testCreateLabel(self):
        r = self.electra.get_repo(("electra", "mutable"))
        label = r.create_label("to_be_deleted", "FF0000")
        self.assertEqual(label.color, "FF0000")
        label.delete()

    def testGetLabel(self):
        r = self.electra.get_repo(("electra", "issues"))
        label = r.get_label("bug")
        self.assertEqual(label.color, "fc2929")

    # @todoAlpha follow-up with issue opened to github for labels with % sign
    # def testGetLabelWithWeirdName(self):
    #     label = self.electra.get_repo("jacquev6/PyGithubIntegrationTests").get_label("space é % space")
    #     self.assertEqual(label.name, "space é % space".decode("utf-8"))

    def testCreateMilestone(self):
        r = self.electra.get_repo(("electra", "mutable"))
        milestone = r.create_milestone("Created by PyGithub")
        self.assertEqual(milestone.title, "Created by PyGithub")
        self.assertEqual(milestone.state, "open")
        self.assertIsNone(milestone.description)
        self.assertIsNone(milestone.due_on)
        milestone.delete()

    def testCreateMilestone_allParameters(self):
        r = self.electra.get_repo(("electra", "mutable"))
        milestone = r.create_milestone("Created by PyGithub", state="closed", description="Body", due_on=datetime.datetime(2014, 8, 1, 0, 0, 0))
        self.assertEqual(milestone.title, "Created by PyGithub")
        self.assertEqual(milestone.state, "closed")
        self.assertEqual(milestone.description, "Body")
        self.assertEqual(milestone.due_on, datetime.datetime(2014, 8, 1, 0, 0, 0))
        milestone.delete()

    def testGetMilestone(self):
        r = self.electra.get_repo(("electra", "issues"))
        milestone = r.get_milestone(1)
        self.assertEqual(milestone.title, "Immutable milestone")

    def testGetMilestones(self):
        r = self.electra.get_repo(("electra", "issues"))
        milestones = r.get_milestones()
        self.assertEqual([m.title for m in milestones], ["Immutable milestone", "Mutable milestone"])

    def testGetMilestones_allParameters(self):
        r = self.electra.get_repo(("electra", "issues"))
        milestones = r.get_milestones(state="open", sort="due_date", direction="asc", per_page=1)
        self.assertEqual([m.title for m in milestones], ["Immutable milestone", "Mutable milestone"])

    def testCreatePull(self):
        r = self.electra.get_repo(("electra", "pulls"))
        p = r.create_pull("Created by PyGithub", "penelope:issue_to_pull", "master")
        self.assertEqual(p.title, "Created by PyGithub")
        self.assertEqual(p.base.label, "electra:master")
        self.assertEqual(p.head.label, "penelope:issue_to_pull")
        self.assertEqual(p.body, None)
        p.edit(state="closed")

    def testCreatePull_allParameters(self):
        r = self.electra.get_repo(("electra", "pulls"))
        p = r.create_pull("Also created by PyGithub", "penelope:issue_to_pull", "master", "Body body body")
        self.assertEqual(p.title, "Also created by PyGithub")
        self.assertEqual(p.base.label, "electra:master")
        self.assertEqual(p.head.label, "penelope:issue_to_pull")
        self.assertEqual(p.body, "Body body body")
        p.edit(state="closed")

    def testGetPulls(self):
        r = self.electra.get_repo(("electra", "pulls"))
        pulls = r.get_pulls()
        self.assertEqual([p.title for p in pulls], ["Mutable pull", "Conflict pull", "Mergeable pull"])

    def testGetPulls_almostAllParameters(self):
        r = self.electra.get_repo(("electra", "pulls"))
        pulls = r.get_pulls(state="open", head="penelope:mergeable", sort="updated", direction="asc")
        self.assertEqual([p.title for p in pulls], ["Mergeable pull"])

    def testGetPulls_base(self):
        r = self.electra.get_repo(("electra", "pulls"))
        pulls = r.get_pulls(base="master", per_page=1)
        self.assertEqual([p.title for p in pulls], ["Mutable pull", "Conflict pull", "Mergeable pull"])

    def testGetPull(self):
        r = self.electra.get_repo(("electra", "pulls"))
        pull = r.get_pull(1)
        self.assertEqual(pull.title, "Merged pull")


class RepositoryKeys(TestCase):
    def testGetKeys(self):
        keys = self.electra.get_repo(("electra", "immutable")).get_keys()
        self.assertEqual([k.title for k in keys], ["immutable-1", "immutable-2"])

    def testGetKey(self):
        k = self.electra.get_repo(("electra", "immutable")).get_key(6)
        self.assertEqual(k.title, "immutable-1")

    def testCreateKey(self):
        k = self.electra.get_repo(("electra", "mutable")).create_key("mutable-1", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkQih2DtSwBzLUtSNYEKULlI5M1qa6vnq42xt9qZpkLav3G9eD/GqJRST+zZMsyfpP62PtiYKXJdLJX2MQIzUgI2PzNy+iMy+ldiTEABYEOCa+BH9+x2R5xXGlmmCPblpamx3kstGtCTa3LSkyIvxbt5vjbXCyThhJaSKyh+42Uedcz7l0y/TODhnkpid/5eiBz6k0VEbFfhM6h71eBdCFpeMJIhGaPTjbKsEjXIK0SRe0v0UQnpXJQkhAINbm+q/2yjt7zwBF74u6tQjRqJK7vQO2k47ZmFMAGeIxS6GheI+JPmwtHkxvfaJjy2lIGX+rt3lkW8xEUxiMTlxeh+0R")
        self.assertEqual(k.title, "mutable-1")
        # @todoAlpha Open ticket to GitHub because k.delete fails because of k.url
        # We would need url=https://api.github.com/repos/electra/mutable/keys/9 to be able to delete it
        # k.delete()
        self.assertTrue(k.url.startswith("http://github.home.jacquev6.net/api/v3/user/keys/"))


class RepositoryPeople(TestCase):
    def testGetCollaborators(self):
        r = self.electra.get_repo(("electra", "mutable"))
        collaborators = r.get_collaborators()
        self.assertEqual([c.login for c in collaborators], ["electra", "zeus", "penelope"])

    def testGetCollaborators_allParameters(self):
        r = self.electra.get_repo(("electra", "mutable"))
        collaborators = r.get_collaborators(per_page=1)
        self.assertEqual([c.login for c in collaborators], ["electra", "zeus", "penelope"])

    def testAddToAndRemoveFromCollaborators(self):
        r = self.electra.get_repo(("electra", "mutable"))
        self.assertTrue(r.has_in_collaborators("penelope"))
        r.remove_from_collaborators("penelope")
        self.assertFalse(r.has_in_collaborators("penelope"))
        r.add_to_collaborators("penelope")
        self.assertTrue(r.has_in_collaborators("penelope"))

    def testGetContributors(self):
        r = self.electra.get_repo(("electra", "contributors"))
        contributors = r.get_contributors()
        self.assertEqual([c.login for c in contributors], ["electra", "penelope", "zeus"])

    def testGetContributors_allParameters(self):
        r = self.electra.get_repo(("electra", "contributors"))
        contributors = r.get_contributors(anon=True, per_page=1)
        self.assertEqual(len(list(contributors)), 4)
        self.assertIsInstance(contributors[0], PyGithub.Blocking.User.User)
        self.assertEqual(contributors[0].login, "electra")
        self.assertIsInstance(contributors[1], PyGithub.Blocking.Repository.Repository.AnonymousContributor)
        self.assertEqual(contributors[1].contributions, 1)
        self.assertEqual(contributors[1].name, "Oedipus")
        self.assertEqual(contributors[1].type, "Anonymous")
        self.assertIsInstance(contributors[2], PyGithub.Blocking.User.User)
        self.assertEqual(contributors[2].login, "penelope")
        self.assertIsInstance(contributors[3], PyGithub.Blocking.User.User)
        self.assertEqual(contributors[3].login, "zeus")

    def testGetForks(self):
        forks = self.electra.get_repo(("electra", "immutable")).get_forks()
        self.assertEqual([f.full_name for f in forks], ["zeus/immutable", "olympus/immutable"])

    def testGetForks_allParameters(self):
        forks = self.electra.get_repo(("electra", "immutable")).get_forks(sort="oldest", per_page=1)
        self.assertEqual([f.full_name for f in forks], ["olympus/immutable", "zeus/immutable"])

    def testGetStargazers(self):
        stargazers = self.electra.get_repo(("electra", "immutable")).get_stargazers()
        self.assertEqual([s.login for s in stargazers], ["penelope", "zeus"])

    def testGetStargazers_allParameters(self):
        stargazers = self.electra.get_repo(("electra", "immutable")).get_stargazers(per_page=1)
        self.assertEqual([s.login for s in stargazers], ["penelope", "zeus"])

    def testGetSubscribers(self):
        subscribers = self.electra.get_repo(("electra", "immutable")).get_subscribers()
        self.assertEqual([s.login for s in subscribers], ["electra", "penelope"])

    def testGetSubscribers_allParameters(self):
        subscribers = self.electra.get_repo(("electra", "immutable")).get_subscribers(per_page=1)
        self.assertEqual([s.login for s in subscribers], ["electra", "penelope"])

    def testGetTeams(self):
        teams = self.zeus.get_repo(("olympus", "immutable")).get_teams()
        self.assertEqual([t.name for t in teams], ["Gods", "Humans"])

    def testGetTeams_allParameters(self):
        teams = self.zeus.get_repo(("olympus", "immutable")).get_teams(per_page=1)
        self.assertEqual([t.name for t in teams], ["Gods", "Humans"])
