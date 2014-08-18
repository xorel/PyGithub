# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class MilestoneAttributes(TestCase):
    def test(self):
        m = self.electra.get_repo(("electra", "issues")).get_milestone(1)
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


class MilestoneDelete(TestCase):
    def test(self):
        m = self.electra.get_repo(("electra", "issues")).create_milestone("Created by PyGithub")
        m.delete()


class MilestoneEdit(TestCase):
    def testTitle(self):
        m = self.electra.get_repo(("electra", "issues")).get_milestone(3)
        self.assertEqual(m.title, "Mutable milestone")
        m.edit(title="Mutable milestone!")
        self.assertEqual(m.title, "Mutable milestone!")
        m.edit(title="Mutable milestone")
        self.assertEqual(m.title, "Mutable milestone")

    def testState(self):
        m = self.electra.get_repo(("electra", "issues")).get_milestone(3)
        self.assertEqual(m.state, "open")
        m.edit(state="closed")
        self.assertEqual(m.state, "closed")
        m.edit(state="open")
        self.assertEqual(m.state, "open")

    def testDescription(self):
        m = self.electra.get_repo(("electra", "issues")).get_milestone(3)
        self.assertEqual(m.description, None)
        m.edit(description="Body of first milestone")
        self.assertEqual(m.description, "Body of first milestone")
        m.edit(description=PyGithub.Blocking.Reset)
        self.assertEqual(m.description, None)

    def testDueOn(self):
        m = self.electra.get_repo(("electra", "issues")).get_milestone(3)
        self.assertEqual(m.due_on, None)
        m.edit(due_on=datetime.datetime(2014, 7, 26, 0, 0, 0))
        self.assertEqual(m.due_on, datetime.datetime(2014, 7, 26, 0, 0, 0))
        m.edit(due_on=PyGithub.Blocking.Reset)
        self.assertEqual(m.due_on, None)


class MilestoneLabels(TestCase):
    def testGetLabels(self):
        m = self.electra.get_repo(("electra", "issues")).get_milestone(1)
        labels = m.get_labels()
        self.assertEqual([l.name for l in labels], ["enhancement", "question"])


class MilestoneUpdate(TestCase):
    def setUpEnterprise(self):  # pragma no cover
        self.setUpTestRepo("electra", "milestone-update").create_milestone("update")
        return Data()

    def test(self):
        repo = self.electra.get_repo(("electra", "milestone-update"))
        self.pause()
        m1 = repo.get_milestone(1)
        m2 = repo.get_milestone(1)
        m2.edit(title="update!")
        self.pause()
        self.assertEqual(m1.title, "update")
        self.assertTrue(m1.update())
        self.assertEqual(m1.title, "update!")
        self.assertFalse(m1.update())
        m2.edit(title="update")
