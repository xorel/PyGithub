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

    def _initAttributes(self, udpated_at=_rcv.Absent, **kwds):
        super(Hook, self)._initAttributes(**kwds)
        self.__udpated_at = _rcv.Attribute("Hook.udpated_at", _rcv.DatetimeConverter, udpated_at)

    def _updateAttributes(self, eTag, udpated_at=_rcv.Absent, **kwds):
        super(Hook, self)._updateAttributes(eTag, **kwds)
        self.__udpated_at.update(udpated_at)

    @property
    def udpated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__udpated_at.needsLazyCompletion)
        return self.__udpated_at.value

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
