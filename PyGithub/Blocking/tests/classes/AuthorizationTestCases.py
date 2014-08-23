# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class AuthorizationAttributes(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        u = self.penelope.get_authenticated_user()
        for a in u.get_authorizations():
            if a.note == "attributes":
                a.delete()
        a = u.create_authorization("attributes", scopes=["repo", "user"], note_url="http://bar.com", client_id="dfb1584c2c0674284875", client_secret="16a529070ec817d87e5b186d966fa935bfad1575")  # Create application manually as electra
        return Data(id=a.id)

    def test(self):
        a = self.penelope.get_authenticated_user().get_authorization(self.data.id)
        self.assertEqual(a.app.name, "authorizations")
        self.assertEqual(a.app.client_id, "dfb1584c2c0674284875")
        self.assertEqual(a.app.url, "http://foo.com")
        self.assertEqual(a.created_at, datetime.datetime(2014, 8, 16, 18, 47, 21))
        self.assertEqual(a.id, 11)
        self.assertEqual(a.note, "attributes")
        self.assertEqual(a.note_url, "http://bar.com")
        self.assertEqual(a.scopes, ["repo", "user"])
        self.assertEqual(a.token, "d8d4d7739c3fbefa5cbab92869e468da4b276bd1")
        self.assertEqual(a.updated_at, datetime.datetime(2014, 8, 16, 18, 47, 21))
        self.assertEqual(a.url, "http://github.home.jacquev6.net/api/v3/authorizations/11")


class AuthorizationDelete(TestCase):
    def test(self):
        a = self.penelope.get_authenticated_user().create_authorization("ephemeral")
        a.delete()


class AuthorizationEdit(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        u = self.penelope.get_authenticated_user()
        for a in u.get_authorizations():
            if a.note == "edit":
                a.delete()
        a = u.create_authorization("edit")
        return Data(id=a.id)

    def testNote(self):
        a = self.penelope.get_authenticated_user().get_authorization(self.data.id)
        self.assertEqual(a.note, "edit")
        a.edit(note="edit!")
        self.assertEqual(a.note, "edit!")
        a.edit(note="edit")
        self.assertEqual(a.note, "edit")

    def testNoteUrl(self):
        a = self.penelope.get_authenticated_user().get_authorization(self.data.id)
        self.assertEqual(a.note_url, None)
        a.edit(note_url="http://foo.bar")
        self.assertEqual(a.note_url, "http://foo.bar")
        a.edit(note_url=PyGithub.Blocking.Reset)
        self.assertEqual(a.note_url, None)

    def testScopes(self):
        a = self.penelope.get_authenticated_user().get_authorization(self.data.id)
        self.assertEqual(a.scopes, [])
        a.edit(scopes=["user", "repo"])
        self.assertEqual(a.scopes, ["user", "repo"])
        a.edit(add_scopes=["gist", "delete_repo"])
        self.assertEqual(a.scopes, ["user", "repo", "gist", "delete_repo"])
        a.edit(remove_scopes=["user", "repo", "gist", "delete_repo"])
        self.assertEqual(a.scopes, [])


class AuthorizationUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        u = self.penelope.get_authenticated_user()
        for a in u.get_authorizations():
            if a.note in ["update", "update!"]:
                a.delete()
        a = u.create_authorization("update")
        return Data(id=a.id)

    def test(self):
        user = self.penelope.get_authenticated_user()
        a1 = user.get_authorization(self.data.id)
        a2 = user.get_authorization(self.data.id)
        a2.edit(note="update!")
        self.pause()
        self.assertEqual(a1.note, "update")
        self.assertTrue(a1.update())
        self.assertEqual(a1.note, "update!")
        self.assertFalse(a1.update())
        a2.edit(note="update")
