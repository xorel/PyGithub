#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import subprocess


def main():
    subprocess.check_call('pep8 --ignore=E501 .', shell=True)

    for line in subprocess.check_output('grep -n "^ *class" $(find PyGithub -name "*.py")', universal_newlines=True, shell=True).split("\n")[:-1]:
        if "(" not in line:
            print("Should this class inherit from object?", line)

    for line in subprocess.Popen('grep -n "assert " PyGithub/Blocking/*.py', universal_newlines=True, shell=True, stdout=subprocess.PIPE).communicate()[0].split("\n")[:-1]:
        print("Seriously, an assert in the main code?", line)

if __name__ == "__main__":
    main()
