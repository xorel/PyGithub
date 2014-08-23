# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import unittest

import MockMockMock

import PyGithub.Blocking
import PyGithub.Blocking._search_result as srch


class OnePageSearchResultTestCase(unittest.TestCase):
    def setUp(self):
        super(OnePageSearchResultTestCase, self).setUp()
        self.mocks = MockMockMock.Engine()
        self.session = self.mocks.create("session")
        self.content = self.mocks.create("content")
        self.response = self.mocks.create("response")
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="a", score=1.), dict(name="b", score=0.75), dict(name="c", score=0.5)]))
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="a", score=1.), dict(name="b", score=0.75), dict(name="c", score=0.5)]))
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="a", score=1.), dict(name="b", score=0.75), dict(name="c", score=0.5)]))
        self.content.expect(self.session.object, dict(name="a")).andReturn(5)
        self.content.expect(self.session.object, dict(name="b")).andReturn(10)
        self.content.expect(self.session.object, dict(name="c")).andReturn(15)
        self.response.expect.links.andReturn(dict())
        self.result = srch.SearchResult(self.content.object, self.session.object, self.response.object)

    def tearDown(self):
        super(OnePageSearchResultTestCase, self).tearDown()
        self.mocks.tearDown()

    def testAttributes(self):
        self.assertEqual(self.result.total_count, 42)
        self.assertEqual(self.result.incomplete_results, False)

    def testElements(self):
        self.assertEqual(self.result.items[0], 5)
        self.assertEqual(self.result.items[1], 10)
        self.assertEqual(self.result.items[2], 15)
        self.assertEqual(self.result.items[-1], 15)
        self.assertEqual(self.result.items[-2], 10)
        self.assertEqual(self.result.items[-3], 5)

    def testSlices(self):
        self.assertEqual(self.result.items[:], [5, 10, 15])
        self.assertEqual(self.result.items[:-7], [])
        self.assertEqual(self.result.items[:-3], [])
        self.assertEqual(self.result.items[:-2], [5])
        self.assertEqual(self.result.items[:-1], [5, 10])
        self.assertEqual(self.result.items[:0], [])
        self.assertEqual(self.result.items[:1], [5])
        self.assertEqual(self.result.items[:2], [5, 10])
        self.assertEqual(self.result.items[:3], [5, 10, 15])
        self.assertEqual(self.result.items[:7], [5, 10, 15])

        self.assertEqual(self.result.items[-7:], [5, 10, 15])
        self.assertEqual(self.result.items[-3:], [5, 10, 15])
        self.assertEqual(self.result.items[-2:], [10, 15])
        self.assertEqual(self.result.items[-1:], [15])
        self.assertEqual(self.result.items[0:], [5, 10, 15])
        self.assertEqual(self.result.items[1:], [10, 15])
        self.assertEqual(self.result.items[2:], [15])
        self.assertEqual(self.result.items[3:], [])
        self.assertEqual(self.result.items[7:], [])

        self.assertEqual(self.result.items[::2], [5, 15])
        self.assertEqual(self.result.items[1::2], [10])
        self.assertEqual(self.result.items[:2:2], [5])
        self.assertEqual(self.result.items[1:2], [10])
        self.assertEqual(self.result.items[1:3], [10, 15])
        self.assertEqual(self.result.items[1:2:2], [10])

        self.assertEqual(self.result.items[::-1], [15, 10, 5])
        self.assertEqual(self.result.items[2::-1], [15, 10, 5])
        self.assertEqual(self.result.items[1::-1], [10, 5])
        self.assertEqual(self.result.items[::-2], [15, 5])
        self.assertEqual(self.result.items[2::-2], [15, 5])
        self.assertEqual(self.result.items[-1::-1], [15, 10, 5])
        self.assertEqual(self.result.items[-1:0:-1], [15, 10])

    def testOutOfRange(self):
        with self.assertRaises(IndexError):
            self.result.items[3]
        with self.assertRaises(IndexError):
            self.result.items[-4]


class PaginationSearchResultTestCase(unittest.TestCase):
    def setUp(self):
        super(PaginationSearchResultTestCase, self).setUp()
        self.mocks = MockMockMock.Engine()
        self.session = self.mocks.create("session")
        self.content = self.mocks.create("content")
        self.response = self.mocks.create("response")
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="a", score=1.), dict(name="b", score=0.75), dict(name="c", score=0.5)]))
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="a", score=1.), dict(name="b", score=0.75), dict(name="c", score=0.5)]))
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="a", score=1.), dict(name="b", score=0.75), dict(name="c", score=0.5)]))
        self.content.expect(self.session.object, dict(name="a")).andReturn(5)
        self.content.expect(self.session.object, dict(name="b")).andReturn(10)
        self.content.expect(self.session.object, dict(name="c")).andReturn(15)
        self.response.expect.links.andReturn(dict(next=dict(url="the-url")))
        self.result = srch.SearchResult(self.content.object, self.session.object, self.response.object)

    def tearDown(self):
        super(PaginationSearchResultTestCase, self).tearDown()
        self.mocks.tearDown()

    def testGrow(self):
        self.session.expect._request("GET", "the-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="d", score=1.), dict(name="e", score=0.75), dict(name="f", score=0.5)]))
        self.content.expect(self.session.object, dict(name="d")).andReturn(20)
        self.content.expect(self.session.object, dict(name="e")).andReturn(25)
        self.content.expect(self.session.object, dict(name="f")).andReturn(30)
        self.response.expect.links.andReturn(dict())
        self.assertEqual(self.result.items[4], 25)
        # Don't try to grow
        with self.assertRaises(IndexError):
            self.result.items[6]

    def testGrowToMaximumForUnboundedIteration(self):
        self.session.expect._request("GET", "the-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="d", score=1.), dict(name="e", score=0.75), dict(name="f", score=0.5)]))
        self.content.expect(self.session.object, dict(name="d")).andReturn(20)
        self.content.expect(self.session.object, dict(name="e")).andReturn(25)
        self.content.expect(self.session.object, dict(name="f")).andReturn(30)
        self.response.expect.links.andReturn(dict(next=dict(url="the-next-url")))
        self.session.expect._request("GET", "the-next-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="g", score=1.), dict(name="h", score=0.75), dict(name="i", score=0.5)]))
        self.content.expect(self.session.object, dict(name="g")).andReturn(35)
        self.content.expect(self.session.object, dict(name="h")).andReturn(40)
        self.content.expect(self.session.object, dict(name="i")).andReturn(45)
        self.response.expect.links.andReturn(dict())
        self.assertEqual(len(list(self.result.items)), 9)

    def testGrowToMaximumForReversedSlice(self):
        self.session.expect._request("GET", "the-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="d", score=1.), dict(name="e", score=0.75), dict(name="f", score=0.5)]))
        self.content.expect(self.session.object, dict(name="d")).andReturn(20)
        self.content.expect(self.session.object, dict(name="e")).andReturn(25)
        self.content.expect(self.session.object, dict(name="f")).andReturn(30)
        self.response.expect.links.andReturn(dict(next=dict(url="the-next-url")))
        self.session.expect._request("GET", "the-next-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[dict(name="g", score=1.), dict(name="h", score=0.75), dict(name="i", score=0.5)]))
        self.content.expect(self.session.object, dict(name="g")).andReturn(35)
        self.content.expect(self.session.object, dict(name="h")).andReturn(40)
        self.content.expect(self.session.object, dict(name="i")).andReturn(45)
        self.response.expect.links.andReturn(dict())
        self.assertEqual(self.result.items[::-1], [45, 40, 35, 30, 25, 20, 15, 10, 5])

    def testStopGrowingOnEmptyPage(self):
        self.session.expect._request("GET", "the-url").andReturn(self.response.object)
        self.response.expect.json().andReturn(dict(total_count=42, incomplete_results=False, items=[]))
        with self.assertRaises(IndexError):
            self.result.items[4]
        # Second time, don't even try to grow
        with self.assertRaises(IndexError):
            self.result.items[4]
