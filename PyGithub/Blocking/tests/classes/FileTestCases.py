# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class FileAttributes(TestCase):
    def test(self):
        f = self.electra.get_repo(("electra", "git-objects")).get_contents("a_blob", ref="db09e03a13f7910b9cae93ca91cd35800e15c695")
        self.assertEqual(f.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
        self.assertEqual(f.encoding, "base64")
        self.assertEqual(f.git_url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/git/blobs/3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(f.html_url, "http://github.home.jacquev6.net/electra/git-objects/blob/db09e03a13f7910b9cae93ca91cd35800e15c695/a_blob")
        self.assertEqual(f.name, "a_blob")
        self.assertEqual(f.path, "a_blob")
        self.assertEqual(f.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(f.size, 20)
        self.assertEqual(f.type, "file")


class FileDelete(TestCase):
    def test(self):
        repo = self.electra.get_repo(("electra", "git-objects"))
        f = repo.get_contents("foo.md")
        c = f.delete("Deleted by PyGithub")
        self.assertEqual(c.message, "Deleted by PyGithub")
        repo.get_git_ref("refs/heads/master").edit("627777afd4859d16e30880f4d8d0a178d99d395c", force=True)

    def test_allParameters(self):
        repo = self.electra.get_repo(("electra", "git-objects"))
        ref = repo.create_git_ref("refs/heads/ephemeral", "627777afd4859d16e30880f4d8d0a178d99d395c")
        f = repo.get_contents("foo.md", ref="ephemeral")
        c = f.delete(
            "Deleted by PyGithub",
            branch="ephemeral",
            # @todoAlpha Normalize structured input. Note that the API does NOT accept an undocumented date
            author={"name": "John Doe", "email": "john@doe.com"},
            committer={"name": "Jane Doe", "email": "jane@doe.com"},
        )
        self.assertEqual(c.message, "Deleted by PyGithub")
        self.assertEqual(c.author.name, "John Doe")
        self.assertEqual(c.committer.name, "Jane Doe")
        ref.delete()


class FileEdit(TestCase):
    def testContent(self):
        repo = self.electra.get_repo(("electra", "git-objects"))
        f = repo.get_contents("foo.md")
        c = f.edit("Modified by PyGithub", "TmV3IGNvbnRlbnQNCg==")
        self.assertEqual(f.content, "TmV3IGNvbnRlbnQNCg==")
        self.assertEqual(f.sha, "03a66315737e55b3e37af882a52df30f9c025197")
        self.assertEqual(c.message, "Modified by PyGithub")
        repo.get_git_ref("refs/heads/master").edit("627777afd4859d16e30880f4d8d0a178d99d395c", force=True)

    def testContent_allParameters(self):
        repo = self.electra.get_repo(("electra", "git-objects"))
        ref = repo.create_git_ref("refs/heads/ephemeral", "627777afd4859d16e30880f4d8d0a178d99d395c")
        f = repo.get_contents("foo.md", ref="ephemeral")
        c = f.edit(
            "Modified by PyGithub",
            "TmV3IGNvbnRlbnQNCg==",
            branch="ephemeral",
            author={"name": "John Doe", "email": "john@doe.com"},
            committer={"name": "Jane Doe", "email": "jane@doe.com"},
        )
        self.assertEqual(f.content, "TmV3IGNvbnRlbnQNCg==")
        self.assertEqual(f.sha, "03a66315737e55b3e37af882a52df30f9c025197")
        self.assertEqual(c.message, "Modified by PyGithub")
        self.assertEqual(c.author.name, "John Doe")
        self.assertEqual(c.committer.name, "Jane Doe")
        ref.delete()
