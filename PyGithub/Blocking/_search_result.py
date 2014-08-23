# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# @todoAlpha Write introduction like in PaginatedList

import sys


class SearchResult(object):
    # @todoAlpha Document
    # @todoAlpha Factorize with PaginatedList

    class Items(object):
        def __init__(self, content, session, r):
            self.__content = content
            self.__session = session
            self.__elements = []
            self.__growWith(r)

        def __getitem__(self, index):
            if isinstance(index, slice):
                start = 0 if index.start is None else index.start
                stop = sys.maxsize if index.stop is None else index.stop
                self.__growToIndex(max(start, stop))
            else:
                self.__growToIndex(index)
            return self.__elements[index]

        def __growToIndex(self, index):
            while len(self.__elements) <= index and self.__url is not None:
                self.__growWith(self.__session._request("GET", self.__url))

        def __growWith(self, r):
            newElements = []
            for v in r.json()["items"]:
                del v["score"]  # @todoAlpha Don't delete the score. Finde a way to keep it without interfering with the content class. See Contributor.contributions and Issue.repository
                newElements.append(self.__content(self.__session, v))
            self.__elements += newElements
            if len(newElements) > 0:
                self.__url = r.links.get("next", {"url": None})["url"]
            else:
                self.__url = None

    def __init__(self, content, session, r):
        self.total_count = r.json()["total_count"]
        self.incomplete_results = r.json()["incomplete_results"]
        self.items = SearchResult.Items(content, session, r)
