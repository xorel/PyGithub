# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class ReleaseAssets(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "release-assets")
        r = repo.create_release("assets")
        self.pause()
        r.upload_asset("text/plain", "readme.txt", "This is the readme")
        self.pause()
        r.upload_asset("text/plain", "changelog.txt", "This is the changelog")
        self.pause()
        return Data(id=r.id)

    def testGetAssets(self):
        r = self.electra.get_repo(("electra", "release-assets")).get_release(self.data.id)
        assets = r.get_assets()
        self.assertEqual([a.name for a in assets], ["changelog.txt", "readme.txt"])

    def testGetAssets_allParameters(self):
        r = self.electra.get_repo(("electra", "release-assets")).get_release(self.data.id)
        assets = r.get_assets(per_page=1)
        self.assertEqual([a.name for a in assets], ["changelog.txt", "readme.txt"])

    def testUploadAsset(self):
        r = self.electra.get_repo(("electra", "release-assets")).get_release(self.data.id)
        # @todoBeta Allow uploading content from file-like object
        # @todoAlpha Test against DotCom because the end point changes for uploads
        a = r.upload_asset("text/plain", "doc.txt", "This is the doc")
        self.assertEqual(a.content_type, "text/plain")
        self.assertEqual(a.name, "doc.txt")
        a.delete()


class ReleaseAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "release-attributes")
        repo.create_git_ref("refs/heads/release_branch", repo.get_git_ref("refs/heads/master").object.sha)
        r = repo.create_release("attributes", target_commitish="release_branch", name="The release", body="The long-awaited release")
        self.pause()
        r.upload_asset("text/plain", "readme.txt", "This is the readme")
        self.pause()
        return Data(id=r.id)

    def test(self):
        r = self.electra.get_repo(("electra", "release-attributes")).get_release(self.data.id)
        self.assertEqual(len(r.assets), 1)
        self.assertEqual(r.assets[0].name, "readme.txt")
        self.assertEqual(r.assets_url, "http://github.home.jacquev6.net/api/v3/repos/electra/release-attributes/releases/36/assets")
        self.assertEqual(r.author.login, "electra")
        self.assertEqual(r.body, "The long-awaited release")
        self.assertEqual(r.body_html, "<p>The long-awaited release</p>")
        self.assertEqual(r.body_text, "The long-awaited release")
        self.assertEqual(r.created_at, datetime.datetime(2014, 8, 16, 22, 31, 45))
        self.assertEqual(r.draft, False)
        self.assertEqual(r.html_url, "http://github.home.jacquev6.net/electra/release-attributes/releases/tag/attributes")
        self.assertEqual(r.id, 36)
        self.assertEqual(r.name, "The release")
        self.assertEqual(r.prerelease, False)
        self.assertEqual(r.published_at, datetime.datetime(2014, 8, 16, 22, 31, 47))
        self.assertEqual(r.tag_name, "attributes")
        self.assertEqual(r.tarball_url, "http://github.home.jacquev6.net/api/v3/repos/electra/release-attributes/tarball/attributes")
        self.assertEqual(r.target_commitish, "release_branch")
        self.assertEqual(r.upload_url, "http://github.home.jacquev6.net/api/uploads/repos/electra/release-attributes/releases/36/assets{?name}")
        self.assertEqual(r.zipball_url, "http://github.home.jacquev6.net/api/v3/repos/electra/release-attributes/zipball/attributes")
        self.assertEqual(r.url, "http://github.home.jacquev6.net/api/v3/repos/electra/release-attributes/releases/36")


class ReleaseDelete(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        self.setUpTestRepo("electra", "release-delete")
        return Data()

    def test(self):
        r = self.electra.get_repo(("electra", "release-delete")).create_release("ephemeral")
        self.pause()
        r.delete()


class ReleaseEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "release-edit")
        r = repo.create_release("edit", name="The name", body="The body")
        self.pause()
        repo.create_git_ref("refs/heads/release_branch", repo.get_git_ref("refs/heads/master").object.sha)
        return Data(id=r.id)

    def testTagName(self):
        r = self.electra.get_repo(("electra", "release-edit")).get_release(self.data.id)
        self.assertEqual(r.tag_name, "edit")
        r.edit(tag_name="editx")
        self.assertEqual(r.tag_name, "editx")
        r.edit(tag_name="edit")
        self.assertEqual(r.tag_name, "edit")

    def testTargetCommitish(self):
        r = self.electra.get_repo(("electra", "release-edit")).get_release(self.data.id)
        self.assertEqual(r.target_commitish, "master")
        r.edit(target_commitish="release_branch")
        self.assertEqual(r.target_commitish, "release_branch")
        r.edit(target_commitish="master")
        self.assertEqual(r.target_commitish, "master")

    def testName(self):
        r = self.electra.get_repo(("electra", "release-edit")).get_release(self.data.id)
        # Not reset-able, even if None by default
        self.assertEqual(r.name, "The name")
        r.edit(name="The name!")
        self.assertEqual(r.name, "The name!")
        r.edit(name="The name")
        self.assertEqual(r.name, "The name")

    def testBody(self):
        r = self.electra.get_repo(("electra", "release-edit")).get_release(self.data.id)
        # Not reset-able, even if None by default
        self.assertEqual(r.body, "The body")
        r.edit(body="The body!")
        self.assertEqual(r.body, "The body!")
        r.edit(body="The body")
        self.assertEqual(r.body, "The body")

    def testDraft(self):
        r = self.electra.get_repo(("electra", "release-edit")).get_release(self.data.id)
        self.assertEqual(r.draft, False)
        r.edit(draft=True)
        self.assertEqual(r.draft, True)
        r.edit(draft=False)
        self.assertEqual(r.draft, False)

    def testPrerelease(self):
        r = self.electra.get_repo(("electra", "release-edit")).get_release(self.data.id)
        self.assertEqual(r.prerelease, False)
        r.edit(prerelease=True)
        self.assertEqual(r.prerelease, True)
        r.edit(prerelease=False)
        self.assertEqual(r.prerelease, False)


class ReleaseUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "release-update")
        r = repo.create_release("update")
        self.pause()
        return Data(id=r.id)

    def test(self):
        repo = self.electra.get_repo(("electra", "release-update"))
        r1 = repo.get_release(self.data.id)
        r2 = repo.get_release(self.data.id)
        r2.edit(tag_name="updatex")
        self.pause()
        self.assertEqual(r1.tag_name, "update")
        self.assertTrue(r1.update())
        self.assertEqual(r1.tag_name, "updatex")
        self.assertFalse(r1.update())
        r2.edit(tag_name="update")
