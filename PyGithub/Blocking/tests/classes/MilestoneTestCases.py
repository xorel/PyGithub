# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class MilestoneAttributes(TestCase):
    @Enterprise("electra")
    def test(self):
        m = self.g.get_repo(("electra", "issues")).get_milestone(1)
        self.assertEqual(m.closed_issues, 2)
        self.assertEqual(m.created_at, datetime.datetime(2014, 8, 4, 3, 9, 47))
        self.assertEqual(m.creator.login, "electra")
        self.assertEqual(m.description, None)
        self.assertEqual(m.due_on, None)
        self.assertEqual(m.id, 17)
        self.assertEqual(m.labels_url, "http://github.home.jacquev6.net/api/v3/repos/electra/issues/milestones/1/labels")
        self.assertEqual(m.number, 1)
        self.assertEqual(m.open_issues, 0)
        self.assertEqual(m.state, "open")
        self.assertEqual(m.title, "Immutable milestone")
        self.assertEqual(m.updated_at, datetime.datetime(2014, 8, 4, 3, 9, 49))
        self.assertEqual(m.url, "http://github.home.jacquev6.net/api/v3/repos/electra/issues/milestones/1")


class MilestoneEdit(TestCase):
    @Enterprise("electra")
    def testTitle(self):
        m = self.g.get_repo(("electra", "issues")).get_milestone(3)
        self.assertEqual(m.title, "Mutable milestone")
        m.edit(title="Mutable milestone!")
        self.assertEqual(m.title, "Mutable milestone!")
        m.edit(title="Mutable milestone")
        self.assertEqual(m.title, "Mutable milestone")

    @Enterprise("electra")
    def testState(self):
        m = self.g.get_repo(("electra", "issues")).get_milestone(3)
        self.assertEqual(m.state, "open")
        m.edit(state="closed")
        self.assertEqual(m.state, "closed")
        m.edit(state="open")
        self.assertEqual(m.state, "open")

    @Enterprise("electra")
    def testDescription(self):
        m = self.g.get_repo(("electra", "issues")).get_milestone(3)
        self.assertEqual(m.description, None)
        m.edit(description="Body of first milestone")
        self.assertEqual(m.description, "Body of first milestone")
        m.edit(description=PyGithub.Blocking.Reset)
        self.assertEqual(m.description, None)

    @Enterprise("electra")
    def testDueOn(self):
        m = self.g.get_repo(("electra", "issues")).get_milestone(3)
        self.assertEqual(m.due_on, None)
        m.edit(due_on="2014-07-26T00:00:00Z")
        self.assertEqual(m.due_on, datetime.datetime(2014, 7, 26, 0, 0))
        m.edit(due_on=PyGithub.Blocking.Reset)
        self.assertEqual(m.due_on, None)


class MilestoneLabels(TestCase):
    @Enterprise("electra")
    def testGetLabels(self):
        m = self.g.get_repo(("electra", "issues")).get_milestone(1)
        labels = m.get_labels()
        self.assertEqual([l.name for l in labels], ["enhancement", "question"])


class MilestoneDelete(TestCase):
    @Enterprise("electra")
    def test(self):
        m = self.g.get_repo(("electra", "issues")).create_milestone("Created by PyGithub")
        m.delete()
