# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import datetime
import logging
import sys
import unittest

import MockMockMock

import PyGithub.Blocking
import PyGithub.Blocking._base_github_object as bgo
import PyGithub.Blocking._receive as rcv
from PyGithub.Blocking.Repository import Repository
from PyGithub.Blocking.User import User
from PyGithub.Blocking.Organization import Organization


stringName = "str" if sys.hexversion >= 0x03000000 else "basestring"


class BaseGithubObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.session = self.mocks.create("session")
        self.result = self.mocks.create("result")
        self.bgoLog = self.mocks.replace("bgo.log")
        self.rcvLog = self.mocks.replace("rcv.log")

    def tearDown(self):
        self.mocks.tearDown()

    def testUnexpectedAttribute(self):
        class Foo(bgo.UpdatableGithubObject):
            pass
        self.bgoLog.expect.info("Foo received an unexpected attribute: 'unexpected' with value 'bar'")
        Foo(self.session.object, dict(url="url", unexpected="bar"), "etag")

    def testUrlAttribute(self):
        o = bgo.UpdatableGithubObject(self.session.object, dict(url="url"), "etag")
        self.assertEqual(o.url, "url")

    def testUrlAttributeAbsent(self):
        self.bgoLog.expect.warn("GitHub API v3 did not return a url")
        o = bgo.UpdatableGithubObject(self.session.object, {}, "etag")
        self.assertIsNone(o.url)
        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            o.update()
        self.assertEqual(cm.exception.args, ("UpdatableGithubObject.url", stringName, None))

    def testUrlAttributeBadlyTyped(self):
        self.rcvLog.expect.warn("Attribute UpdatableGithubObject.url is expected to be a " + stringName + " but GitHub API v3 returned 42")
        o = bgo.UpdatableGithubObject(self.session.object, dict(url=42), "etag")
        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            o.url
        self.assertEqual(cm.exception.args[:3], ("UpdatableGithubObject.url", stringName, 42))

    def testUpdateNothing(self):
        o = bgo.UpdatableGithubObject(self.session.object, dict(url="url"), "etag")
        self.session.expect._request("GET", "url", headers={"If-None-Match": "etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(304)
        self.assertFalse(o.update())

    def testUpdateSomething(self):
        o = bgo.UpdatableGithubObject(self.session.object, dict(url="url"), "etag")
        self.session.expect._request("GET", "url", headers={"If-None-Match": "etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn({"ETag": "new-etag"})
        self.result.expect.json().andReturn(dict(url="new-url"))
        self.assertTrue(o.update())

    def testUpdateTwice(self):
        o = bgo.UpdatableGithubObject(self.session.object, dict(url="url"), "etag")
        self.session.expect._request("GET", "url", headers={"If-None-Match": "etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn({"ETag": "new-etag"})
        self.result.expect.json().andReturn(dict(url="new-url"))
        self.assertTrue(o.update())
        self.session.expect._request("GET", "new-url", headers={"If-None-Match": "new-etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(304)
        self.assertFalse(o.update())

    def testUpdateWithoutUrl(self):
        o = bgo.UpdatableGithubObject(self.session.object, dict(url="url"), "etag")
        self.session.expect._request("GET", "url", headers={"If-None-Match": "etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn({"ETag": "new-etag"})
        self.result.expect.json().andReturn(dict())
        self.bgoLog.expect.warn("GitHub API v3 did not return a url")
        self.assertTrue(o.update())

    def testCompleteLazily(self):
        o = bgo.UpdatableGithubObject(self.session.object, dict(url="url"), None)
        self.session.expect._request("GET", "url", headers={"If-None-Match": None}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(304)
        o._completeLazily(True)


class GithubObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.session = self.mocks.create("session")
        self.result = self.mocks.create("result")
        self.bgoLog = self.mocks.replace("bgo.log")
        self.rcvLog = self.mocks.replace("rcv.log")

    def tearDown(self):
        self.mocks.tearDown()

    def test_FullObject_AttributePresent_NoLazyCompletion(self):
        r = Repository(self.session.object, dict(url="url", name="name"), "etag")
        self.assertEqual(r.name, "name")

    def test_FullObject_AttributeNone_NoLazyCompletion(self):
        r = Repository(self.session.object, dict(url="url", name=None), "etag")
        self.assertEqual(r.name, None)

    def test_FullObject_AttributeAbsent_NoLazyCompletion(self):
        r = Repository(self.session.object, dict(url="url"), "etag")
        self.assertEqual(r.name, None)

    def test_PartialObject_AttributePresent_NoLazyCompletion(self):
        r = Repository(self.session.object, dict(url="url", name="name"), None)
        self.assertEqual(r.name, "name")

    def test_PartialObject_AttributeNone_NoLazyCompletion(self):
        r = Repository(self.session.object, dict(url="url", name=None), None)
        self.assertEqual(r.name, None)

    def test_PartialObject_AttributeAbsent_LazyCompletion(self):
        r = Repository(self.session.object, dict(url="url"), None)
        self.session.expect._request("GET", "url", headers={"If-None-Match": None}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn(dict(ETag="etag"))
        self.result.expect.json().andReturn(dict(url="url", name="name"))
        self.assertEqual(r.name, "name")

    def test_PartialObject_AttributeAbsent_LazyCompletion_AttributeNone_NoLazyCompletion(self):
        r = Repository(self.session.object, dict(url="url"), None)
        self.session.expect._request("GET", "url", headers={"If-None-Match": None}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn(dict(ETag="etag"))
        self.result.expect.json().andReturn(dict(url="url", name=None))
        self.assertEqual(r.name, None)
        self.assertEqual(r.name, None)

    def test_PartialObject_AttributeAbsent_LazyCompletion_AttributeAbsent_NoLazyCompletion(self):
        r = Repository(self.session.object, dict(url="url"), None)
        self.session.expect._request("GET", "url", headers={"If-None-Match": None}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn(dict(ETag="etag"))
        self.result.expect.json().andReturn(dict(url="url"))
        self.assertEqual(r.name, None)
        self.assertEqual(r.name, None)

    def testUpdatePreservesIdentityOfClassAttributes(self):
        r = Repository(self.session.object, dict(url="url", parent=dict(url="parent_url", name="42")), "etag")
        p = r.parent
        self.assertEqual(r.parent.name, "42")
        self.session.expect._request("GET", "url", headers={"If-None-Match": "etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn(dict(ETag="new-etag"))
        self.result.expect.json().andReturn(dict(url="url", parent=dict(url="parent_url", name="57")))
        self.assertTrue(r.update())
        self.assertIs(r.parent, p)
        self.assertEqual(r.parent.name, "57")

    def testUpdatePreservesIdentityOfStructAttributes(self):
        u = User(self.session.object, dict(url="url", plan=dict(private_repos=42)), "etag")
        p = u.plan
        self.assertEqual(u.plan.private_repos, 42)
        self.session.expect._request("GET", "url", headers={"If-None-Match": "etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn(dict(ETag="new-etag"))
        self.result.expect.json().andReturn(dict(url="url", plan=dict(private_repos=57)))
        self.assertTrue(u.update())
        self.assertIs(u.plan, p)
        self.assertEqual(u.plan.private_repos, 57)

    def testUpdatePreservesIdentityOfUnionAttributes(self):
        r = Repository(self.session.object, dict(url="url", owner=dict(url="url", type="User", id=42)), "etag")
        o = r.owner
        self.assertIsInstance(r.owner, User)
        self.assertEqual(r.owner.id, 42)
        self.session.expect._request("GET", "url", headers={"If-None-Match": "etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn(dict(ETag="new-etag"))
        self.result.expect.json().andReturn(dict(url="url", owner=dict(url="url", type="User", id=57)))
        self.assertTrue(r.update())
        self.assertIs(r.owner, o)
        self.assertEqual(r.owner.id, 57)

    def testUpdateChangesTypeOfUnionAttributes(self):
        r = Repository(self.session.object, dict(url="url", owner=dict(url="url", type="User", id=42)), "etag")
        o = r.owner
        self.assertIsInstance(r.owner, User)
        self.assertEqual(r.owner.id, 42)
        self.session.expect._request("GET", "url", headers={"If-None-Match": "etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(200)
        self.result.expect.headers.andReturn(dict(ETag="new-etag"))
        self.result.expect.json().andReturn(dict(url="url", owner=dict(url="url", type="Organization", id=57)))
        self.assertTrue(r.update())
        self.assertIsNot(r.owner, o)
        self.assertIsInstance(r.owner, Organization)
        self.assertEqual(r.owner.id, 57)

    def testUpdateNotNeededAfterEdit(self):
        r = Repository(self.session.object, dict(url="url", owner=dict(url="url", type="User", id=42)), "etag")
        self.session.expect._request("PATCH", "url", postArguments=dict(name="foo")).andReturn(self.result.object)
        self.result.expect.headers.andReturn(dict(ETag="new-etag"))
        self.result.expect.json().andReturn(dict(url="url", owner=dict(url="url", type="Organization", id=57)))
        r.edit(name="foo")
        self.session.expect._request("GET", "url", headers={"If-None-Match": "new-etag"}).andReturn(self.result.object)
        self.result.expect.status_code.andReturn(304)
        self.assertFalse(r.update())
