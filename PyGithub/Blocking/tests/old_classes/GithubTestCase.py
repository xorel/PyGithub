# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import textwrap
import datetime

import PyGithub.Blocking
import PyGithub.Blocking.tests.Framework as Framework


class GithubTestCase(Framework.SimpleLoginTestCase):
    def testGetPublicGists(self):
        gists = self.g.get_public_gists()
        self.assertEqual(gists[0].created_at, datetime.datetime(2014, 7, 12, 2, 35, 47))
        self.assertEqual(gists[0].updated_at, datetime.datetime(2014, 7, 12, 2, 35, 48))
        self.assertEqual(gists[1].created_at, datetime.datetime(2014, 7, 12, 2, 35, 18))
        self.assertEqual(gists[1].updated_at, datetime.datetime(2014, 7, 12, 2, 35, 19))
        self.assertEqual(gists[5].created_at, datetime.datetime(2014, 7, 12, 2, 32, 23))
        self.assertEqual(gists[5].updated_at, datetime.datetime(2014, 7, 12, 2, 32, 24))

    def testGetPublicGists_allParameters(self):
        # I don't really understand the effect of the 'since' parameter
        gists = self.g.get_public_gists(since=datetime.datetime(2014, 7, 12, 2, 30, 0), per_page=10)
        self.assertEqual(len(gists[:]), 33)
        self.assertEqual(gists[0].created_at, datetime.datetime(2014, 7, 12, 2, 45, 23))
        self.assertEqual(gists[0].updated_at, datetime.datetime(2014, 7, 12, 2, 45, 24))
        self.assertEqual(gists[32].created_at, datetime.datetime(2010, 4, 24, 23, 17, 32))
        self.assertEqual(gists[32].updated_at, datetime.datetime(2014, 7, 12, 2, 42, 25))

    def testCreateAnonymousGist(self):
        g = self.g.create_anonymous_gist(files={"foo.txt": {"content": "barbaz"}})
        self.assertIsNone(g.owner)
        self.assertIsNone(g.user)
        self.assertEqual(g.public, False)
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            g.delete()

    def testCreateAnonymousGist_allParameters(self):
        g = self.g.create_anonymous_gist(files={"foo.txt": {"content": "barbaz"}}, description="Created by PyGithub", public=True)
        self.assertIsNone(g.owner)
        self.assertIsNone(g.user)
        self.assertEqual(g.description, "Created by PyGithub")
        self.assertEqual(g.public, True)
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            g.delete()
