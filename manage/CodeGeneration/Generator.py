# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import glob
import itertools
import os

import CodeGeneration.CodeGenerator
import CodeGeneration.TestGenerator
import CodeGeneration.RstGenerator


class Generator(object):
    def __init__(self, definition):
        self.__definition = definition
        self.__validFiles = set()
        self.codeGenerator = CodeGeneration.CodeGenerator.CodeGenerator()
        self.testGenerator = CodeGeneration.TestGenerator.TestGenerator()
        self.rstGenerator = CodeGeneration.RstGenerator.RstGenerator()

    def generate(self):
        self.__writeFileEvenIfExists(self.rstGenerator.generateApis(self.__definition.endPoints), os.path.join("doc", "reference", "apis.rst"))
        self.__writeFileEvenIfExists(self.testGenerator.generateAll(self.__definition.classes), os.path.join("PyGithub", "Blocking", "tests", "classes", "all.py"))
        self.__writeFileEvenIfExists(self.testGenerator.generateAllImports(self.__definition.classes), os.path.join("PyGithub", "Blocking", "tests", "classes", "imports.py"))

        for klass in self.__definition.classes:
            self.__writeFileEvenIfExists(self.rstGenerator.generateClass(klass), os.path.join("doc", "reference", "classes", klass.simpleName + ".rst"))
            self.__writeFileEvenIfExists(self.codeGenerator.generateClass(klass), os.path.join("PyGithub", "Blocking", klass.simpleName + ".py"))
            self.__writeFileUnlessExists(self.testGenerator.generateClass(klass), os.path.join("PyGithub", "Blocking", "tests", "classes", klass.simpleName + "TestCases.py"))
        self.__validFiles.update((glob.glob("PyGithub/Blocking/_*.py")))
        for f in itertools.chain(glob.glob("doc/reference/classes/*.rst"), glob.glob("PyGithub/Blocking/*.py"), glob.glob("PyGithub/Blocking/tests/classes/*TestCases.py")):
            if f not in self.__validFiles:
                os.unlink(f)

    def __writeFileUnlessExists(self, content, output):
        self.__validFiles.add(output)
        if not os.path.exists(output):
            if output.endswith(".py"):
                header = [
                    "# -*- coding: utf-8 -*-",
                    "",
                    "# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>",
                    "",
                ]
            self.__writeFile(itertools.chain(header, content), output)  # pragma no cover

    def __writeFileEvenIfExists(self, content, output):
        self.__validFiles.add(output)
        if output.endswith(".py"):
            header = [
                "# -*- coding: utf-8 -*-",
                "",
                "# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>",
                "",
                "# ######################################################################",
                "# #### This file is generated. Manual changes will likely be lost. #####",
                "# ######################################################################",
                "",
            ]
        elif output.endswith(".rst"):
            header = [
                ".. ########################################################################",
                "   ###### This file is generated. Manual changes will likely be lost. #####",
                "   ########################################################################",
                "",
            ]
        else:
            raise Exception("Unable to write the 'generated' warning")  # pragma no cover
        self.__writeFile(itertools.chain(header, content), output)

    def __writeFile(self, content, output):
        content = list(content)  # To make sure all exceptions are raised before opening the file
        with open(output, "w") as f:
            f.write("\n".join(content))
            if content[-1] != "":
                f.write("\n")
