# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Hook(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.create_hook`
      * :meth:`.Repository.get_hook`
      * :meth:`.Repository.get_hooks`

    Methods accepting instances of this class as parameter: none.
    """

    class Response(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Hook.last_response`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, code=None, message=None, status=None, **kwds):
            super(Hook.Response, self)._initAttributes(**kwds)
            self.__code = _rcv.Attribute("Hook.Response.code", _rcv.IntConverter, code)
            self.__message = _rcv.Attribute("Hook.Response.message", _rcv.StringConverter, message)
            self.__status = _rcv.Attribute("Hook.Response.status", _rcv.StringConverter, status)

        def _updateAttributes(self, code=None, message=None, status=None, **kwds):
            super(Hook.Response, self)._updateAttributes(**kwds)
            self.__code.update(code)
            self.__message.update(message)
            self.__status.update(status)

        @property
        def code(self):
            """
            :type: :class:`int`
            """
            return self.__code.value

        @property
        def message(self):
            """
            :type: :class:`string`
            """
            return self.__message.value

        @property
        def status(self):
            """
            :type: :class:`string`
            """
            return self.__status.value

    def _initAttributes(self, active=_rcv.Absent, config=_rcv.Absent, created_at=_rcv.Absent, events=_rcv.Absent, id=_rcv.Absent, last_response=_rcv.Absent, name=_rcv.Absent, test_url=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
        super(Hook, self)._initAttributes(**kwds)
        self.__active = _rcv.Attribute("Hook.active", _rcv.BoolConverter, active)
        self.__config = _rcv.Attribute("Hook.config", _rcv.DictConverter(_rcv.StringConverter, _rcv.AnyConverter), config)
        self.__created_at = _rcv.Attribute("Hook.created_at", _rcv.DatetimeConverter, created_at)
        self.__events = _rcv.Attribute("Hook.events", _rcv.ListConverter(_rcv.StringConverter), events)
        self.__id = _rcv.Attribute("Hook.id", _rcv.IntConverter, id)
        self.__last_response = _rcv.Attribute("Hook.last_response", _rcv.StructureConverter(self.Session, Hook.Response), last_response)
        self.__name = _rcv.Attribute("Hook.name", _rcv.StringConverter, name)
        self.__test_url = _rcv.Attribute("Hook.test_url", _rcv.StringConverter, test_url)
        self.__updated_at = _rcv.Attribute("Hook.updated_at", _rcv.DatetimeConverter, updated_at)

    def _updateAttributes(self, eTag, active=_rcv.Absent, config=_rcv.Absent, created_at=_rcv.Absent, events=_rcv.Absent, id=_rcv.Absent, last_response=_rcv.Absent, name=_rcv.Absent, test_url=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
        super(Hook, self)._updateAttributes(eTag, **kwds)
        self.__active.update(active)
        self.__config.update(config)
        self.__created_at.update(created_at)
        self.__events.update(events)
        self.__id.update(id)
        self.__last_response.update(last_response)
        self.__name.update(name)
        self.__test_url.update(test_url)
        self.__updated_at.update(updated_at)

    @property
    def active(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__active.needsLazyCompletion)
        return self.__active.value

    @property
    def config(self):
        """
        :type: :class:`dict` of :class:`string` to :class:`any`
        """
        self._completeLazily(self.__config.needsLazyCompletion)
        return self.__config.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def events(self):
        """
        :type: :class:`list` of :class:`string`
        """
        self._completeLazily(self.__events.needsLazyCompletion)
        return self.__events.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def last_response(self):
        """
        :type: :class:`.Hook.Response`
        """
        self._completeLazily(self.__last_response.needsLazyCompletion)
        return self.__last_response.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def test_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__test_url.needsLazyCompletion)
        return self.__test_url.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self._url

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo/hooks/:id <http://developer.github.com/v3/repos/hooks#delete-a-hook>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self._url)
        r = self.Session._request("DELETE", url)

    def edit(self, config=None, events=None, add_events=None, remove_events=None, active=None):
        """
        Calls the `PATCH /repos/:owner/:repo/hooks/:id <http://developer.github.com/v3/repos/hooks#edit-a-hook>`__ end point.

        This is the only method calling this end point.

        :param config: optional :class:`dict`
        :param events: optional :class:`list` of :class:`string`
        :param add_events: optional :class:`list` of :class:`string`
        :param remove_events: optional :class:`list` of :class:`string`
        :param active: optional :class:`bool`
        :rtype: None
        """

        if config is not None:
            config = _snd.normalizeDict(config)
        if events is not None:
            events = _snd.normalizeList(_snd.normalizeString, events)
        if add_events is not None:
            add_events = _snd.normalizeList(_snd.normalizeString, add_events)
        if remove_events is not None:
            remove_events = _snd.normalizeList(_snd.normalizeString, remove_events)
        if active is not None:
            active = _snd.normalizeBool(active)

        url = uritemplate.expand(self._url)
        postArguments = _snd.dictionary(active=active, add_events=add_events, config=config, events=events, remove_events=remove_events)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def ping(self):
        """
        Calls the `POST /repos/:owner/:repo/hooks/:id/pings <http://developer.github.com/v3/repos/hooks#ping-a-hook>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = "https://api.github.com/repos/{owner}/{repo}/hooks/{id}/pings"
        r = self.Session._request("POST", url)

    def test(self):
        """
        Calls the `POST /repos/:owner/:repo/hooks/:id/tests <http://developer.github.com/v3/repos/hooks#test-a-push-hook>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = "https://api.github.com/repos/{owner}/{repo}/hooks/{id}/tests"
        r = self.Session._request("POST", url)

    def update(self):
        """
        Makes a `conditional request <http://developer.github.com/v3/#conditional-requests>`_ and updates the object.
        Returns True if the object was updated.

        :rtype: :class:`bool`
        """
        return self._update()
