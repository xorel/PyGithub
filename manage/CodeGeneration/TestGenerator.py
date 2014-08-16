# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000


class TestGenerator:
    def generateAll(self, classes):
        for klass in classes:
            yield "from PyGithub.Blocking.tests.classes.{}TestCases import *".format(klass.simpleName)

    def generateClass(self, klass):  # pragma no cover
        yield "from PyGithub.Blocking.tests.Framework import *"
