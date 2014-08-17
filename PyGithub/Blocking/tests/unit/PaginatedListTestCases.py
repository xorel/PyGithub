# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import unittest

import MockMockMock

import PyGithub.Blocking
import PyGithub.Blocking._paginated_list as pgl


class OnePageTestCase(unittest.TestCase):
    def setUp(self):
        super(OnePageTestCase, self).setUp()
        self.mocks = MockMockMock.Engine()
        self.session = self.mocks.create("session")
        self.content = self.mocks.create("content")
        self.response = self.mocks.create("response")
        self.response.expect.json().andReturn(["a", "b", "c"])
        self.content.expect(self.session.object, "a").andReturn(5)
        self.content.expect(self.session.object, "b").andReturn(10)
        self.content.expect(self.session.object, "c").andReturn(15)
        self.response.expect.links.andReturn(dict())
        self.list = pgl.PaginatedList(self.content.object, self.session.object, self.response.object)

    def tearDown(self):
        super(OnePageTestCase, self).tearDown()
        self.mocks.tearDown()

    def testElements(self):
        self.assertEqual(self.list[0], 5)
        self.assertEqual(self.list[1], 10)
        self.assertEqual(self.list[2], 15)
        self.assertEqual(self.list[-1], 15)
        self.assertEqual(self.list[-2], 10)
        self.assertEqual(self.list[-3], 5)

    def testSlices(self):
        self.assertEqual(self.list[:], [5, 10, 15])
        self.assertEqual(self.list[:-7], [])
        self.assertEqual(self.list[:-3], [])
        self.assertEqual(self.list[:-2], [5])
        self.assertEqual(self.list[:-1], [5, 10])
        self.assertEqual(self.list[:0], [])
        self.assertEqual(self.list[:1], [5])
        self.assertEqual(self.list[:2], [5, 10])
        self.assertEqual(self.list[:3], [5, 10, 15])
        self.assertEqual(self.list[:7], [5, 10, 15])

        self.assertEqual(self.list[-7:], [5, 10, 15])
        self.assertEqual(self.list[-3:], [5, 10, 15])
        self.assertEqual(self.list[-2:], [10, 15])
        self.assertEqual(self.list[-1:], [15])
        self.assertEqual(self.list[0:], [5, 10, 15])
        self.assertEqual(self.list[1:], [10, 15])
        self.assertEqual(self.list[2:], [15])
        self.assertEqual(self.list[3:], [])
        self.assertEqual(self.list[7:], [])

        self.assertEqual(self.list[::2], [5, 15])
        self.assertEqual(self.list[1::2], [10])
        self.assertEqual(self.list[:2:2], [5])
        self.assertEqual(self.list[1:2], [10])
        self.assertEqual(self.list[1:3], [10, 15])
        self.assertEqual(self.list[1:2:2], [10])

        self.assertEqual(self.list[::-1], [15, 10, 5])
        self.assertEqual(self.list[2::-1], [15, 10, 5])
        self.assertEqual(self.list[1::-1], [10, 5])
        self.assertEqual(self.list[::-2], [15, 5])
        self.assertEqual(self.list[2::-2], [15, 5])
        self.assertEqual(self.list[-1::-1], [15, 10, 5])
        self.assertEqual(self.list[-1:0:-1], [15, 10])

    def testOutOfRange(self):
        with self.assertRaises(IndexError):
            self.list[3]
        with self.assertRaises(IndexError):
            self.list[-4]


class PaginationTestCase(unittest.TestCase):
    def setUp(self):
        super(PaginationTestCase, self).setUp()
        self.mocks = MockMockMock.Engine()
        self.session = self.mocks.create("session")
        self.content = self.mocks.create("content")
        self.response = self.mocks.create("response")
        self.response.expect.json().andReturn(["a", "b", "c"])
        self.content.expect(self.session.object, "a").andReturn(5)
        self.content.expect(self.session.object, "b").andReturn(10)
        self.content.expect(self.session.object, "c").andReturn(15)
        self.response.expect.links.andReturn(dict(next=dict(url="the-url")))
        self.list = pgl.PaginatedList(self.content.object, self.session.object, self.response.object)

    def tearDown(self):
        super(PaginationTestCase, self).tearDown()
        self.mocks.tearDown()

    def testGrow(self):
        self.session.expect._request("GET", "the-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(["d", "e", "f"])
        self.content.expect(self.session.object, "d").andReturn(20)
        self.content.expect(self.session.object, "e").andReturn(25)
        self.content.expect(self.session.object, "f").andReturn(30)
        self.response.expect.links.andReturn(dict())
        self.assertEqual(self.list[4], 25)
        # Don't try to grow
        with self.assertRaises(IndexError):
            self.list[6]

    def testGrowToMaximumForUnboundedIteration(self):
        self.session.expect._request("GET", "the-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(["d", "e", "f"])
        self.content.expect(self.session.object, "d").andReturn(20)
        self.content.expect(self.session.object, "e").andReturn(25)
        self.content.expect(self.session.object, "f").andReturn(30)
        self.response.expect.links.andReturn(dict(next=dict(url="the-next-url")))
        self.session.expect._request("GET", "the-next-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(["g", "h", "i"])
        self.content.expect(self.session.object, "g").andReturn(35)
        self.content.expect(self.session.object, "h").andReturn(40)
        self.content.expect(self.session.object, "i").andReturn(45)
        self.response.expect.links.andReturn(dict())
        self.assertEqual(len(list(self.list)), 9)

    def testGrowToMaximumForReversedSlice(self):
        self.session.expect._request("GET", "the-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(["d", "e", "f"])
        self.content.expect(self.session.object, "d").andReturn(20)
        self.content.expect(self.session.object, "e").andReturn(25)
        self.content.expect(self.session.object, "f").andReturn(30)
        self.response.expect.links.andReturn(dict(next=dict(url="the-next-url")))
        self.session.expect._request("GET", "the-next-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(["g", "h", "i"])
        self.content.expect(self.session.object, "g").andReturn(35)
        self.content.expect(self.session.object, "h").andReturn(40)
        self.content.expect(self.session.object, "i").andReturn(45)
        self.response.expect.links.andReturn(dict())
        self.assertEqual(self.list[::-1], [45, 40, 35, 30, 25, 20, 15, 10, 5])

    def testStopGrowingOnEmptyPage(self):
        self.session.expect._request("GET", "the-url").andReturn(self.response.object)
        self.response.expect.json().andReturn([])
        with self.assertRaises(IndexError):
            self.list[4]
        # Second time, don't even try to grow
        with self.assertRaises(IndexError):
            self.list[4]
