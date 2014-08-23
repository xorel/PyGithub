# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import unittest
import logging

from PyGithub.Blocking.tests.automated import *

if __name__ == "__main__":
    logging.getLogger("PyGithub").addHandler(logging.StreamHandler())  # pragma no cover
    unittest.main()  # pragma no cover
