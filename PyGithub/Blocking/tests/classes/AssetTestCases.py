# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class AssetAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "asset-attributes")
        r = repo.create_release("assets")
        self.pause()
        a = r.upload_asset("text/plain", "readme.txt", "This is the readme")
        self.pause()
        return Data(id=a.id)

    def test(self):
        a = self.electra.get_repo(("electra", "asset-attributes")).get_release_asset(self.data.id)
        self.assertEqual(a.browser_download_url, None)  # I don't know if this attribute is ever returned, but it is documented
        self.assertEqual(a.content_type, "text/plain")
        self.assertEqual(a.created_at, datetime.datetime(2014, 8, 16, 22, 26, 12))
        self.assertEqual(a.download_count, 0)
        self.assertEqual(a.id, 10)
        self.assertEqual(a.label, None)
        self.assertEqual(a.name, "readme.txt")
        self.assertEqual(a.size, 18)
        self.assertEqual(a.state, "uploaded")
        self.assertEqual(a.updated_at, datetime.datetime(2014, 8, 16, 22, 26, 12))
        self.assertEqual(a.uploader.login, "electra")


class AssetDelete(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "asset-delete")
        r = repo.create_release("assets")
        return Data(id=r.id)

    def test(self):
        r = self.electra.get_repo(("electra", "asset-delete")).get_release(self.data.id)
        a = r.upload_asset("text/plain", "readme.txt", "This is the readme")
        self.pause()
        a.delete()


class AssetEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        repo = self.setUpTestRepo("electra", "asset-edit")
        r = repo.create_release("assets")
        self.pause()
        a = r.upload_asset("text/plain", "readme.txt", "This is the readme")
        self.pause()
        a.edit(a.name, label="foo")
        self.pause()
        return Data(id=a.id)

    def testName(self):
        a = self.electra.get_repo(("electra", "asset-edit")).get_release_asset(self.data.id)
        self.assertEqual(a.name, "readme.txt")
        a.edit(name="changelog.txt")
        self.assertEqual(a.name, "changelog.txt")
        a.edit(name="readme.txt")
        self.assertEqual(a.name, "readme.txt")

    def testLabel(self):
        a = self.electra.get_repo(("electra", "asset-edit")).get_release_asset(self.data.id)
        # Not reset-able even if None by default
        self.assertEqual(a.label, "foo")
        a.edit(a.name, label="bar")
        self.assertEqual(a.label, "bar")
        a.edit(a.name, label="foo")
        self.assertEqual(a.label, "foo")
