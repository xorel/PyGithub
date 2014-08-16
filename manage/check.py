#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import subprocess


def main():
    subprocess.check_call([
        "pep8", "--ignore=E501", ".",
    ])

    for line in subprocess.check_output([
        "git", "grep", "-n", "^ *class ", "--", "PyGithub/**.py"

    ], universal_newlines=True).split("\n"):
        if "(" not in line and line != "":
            print("Should this class inherit from object?", line)

if __name__ == "__main__":
    main()
