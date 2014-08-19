# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GistCommentAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        u = self.electra.get_authenticated_user()
        for g in u.get_gists():
            if g.description == "gist-comment-attributes":
                g.delete()
        g = self.electra.get_authenticated_user().create_gist(files={"foo.txt": {"content": "barbaz"}}, public=True, description="gist-comment-attributes")
        self.pause()
        c = g.create_comment("attributes")
        self.pause()
        return Data(gist_id=g.id, comment_id=c.id)

    def test(self):
        g = self.electra.get_gist(self.data.gist_id)
        c = g.get_comment(self.data.comment_id)
        self.assertEqual(c.body, "attributes")
        self.assertEqual(c.body_html, "<p>attributes</p>")
        self.assertEqual(c.body_text, "attributes")
        self.assertEqual(c.created_at, datetime.datetime(2014, 8, 19, 14, 28, 21))
        self.assertEqual(c.id, 6)
        self.assertEqual(c.updated_at, datetime.datetime(2014, 8, 19, 14, 28, 21))
        self.assertEqual(c.user.login, "electra")
        self.assertEqual(c.url, "http://github.home.jacquev6.net/api/v3/gists/0495f0700517db101a9a/comments/6")


class GistCommentDelete(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        u = self.electra.get_authenticated_user()
        for g in u.get_gists():
            if g.description == "gist-comment-delete":
                g.delete()
        g = self.electra.get_authenticated_user().create_gist(files={"foo.txt": {"content": "barbaz"}}, public=True, description="gist-comment-delete")
        self.pause()
        return Data(gist_id=g.id)

    def testBody(self):
        g = self.electra.get_gist(self.data.gist_id)
        c = g.create_comment("ephemeral")
        c.delete()


class GistCommentEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        u = self.electra.get_authenticated_user()
        for g in u.get_gists():
            if g.description == "gist-comment-edit":
                g.delete()
        g = self.electra.get_authenticated_user().create_gist(files={"foo.txt": {"content": "barbaz"}}, public=True, description="gist-comment-edit")
        self.pause()
        c = g.create_comment("edit")
        self.pause()
        return Data(gist_id=g.id, comment_id=c.id)

    def testBody(self):
        g = self.electra.get_gist(self.data.gist_id)
        c = g.get_comment(self.data.comment_id)
        self.assertEqual(c.body, "edit")
        c.edit("edit!")
        self.assertEqual(c.body, "edit!")
        c.edit("edit")
        self.assertEqual(c.body, "edit")


class GistCommentUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        u = self.electra.get_authenticated_user()
        for g in u.get_gists():
            if g.description == "gist-comment-update":
                g.delete()
        g = self.electra.get_authenticated_user().create_gist(files={"foo.txt": {"content": "barbaz"}}, public=True, description="gist-comment-update")
        self.pause()
        c = g.create_comment("update")
        self.pause()
        return Data(gist_id=g.id, comment_id=c.id)

    def test(self):
        g = self.electra.get_gist(self.data.gist_id)
        c1 = g.get_comment(self.data.comment_id)
        c2 = g.get_comment(self.data.comment_id)
        c2.edit(body="update!")
        self.pause()
        self.assertEqual(c1.body, "update")
        self.assertTrue(c1.update())
        self.assertEqual(c1.body, "update!")
        self.assertFalse(c1.update())
        c2.edit(body="update")
