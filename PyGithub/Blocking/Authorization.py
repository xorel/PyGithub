# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Authorization(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.create_authorization`
      * :meth:`.AuthenticatedUser.get_authorization`
      * :meth:`.AuthenticatedUser.get_authorizations`
      * :meth:`.AuthenticatedUser.get_or_create_authorization`

    Methods accepting instances of this class as parameter: none.
    """

    class Application(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Authorization.app`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, client_id=None, name=None, url=None, **kwds):
            super(Authorization.Application, self)._initAttributes(**kwds)
            self.__client_id = _rcv.Attribute("Authorization.Application.client_id", _rcv.StringConverter, client_id)
            self.__name = _rcv.Attribute("Authorization.Application.name", _rcv.StringConverter, name)
            self.__url = _rcv.Attribute("Authorization.Application.url", _rcv.StringConverter, url)

        def _updateAttributes(self, client_id=None, name=None, url=None, **kwds):
            super(Authorization.Application, self)._updateAttributes(**kwds)
            self.__client_id.update(client_id)
            self.__name.update(name)
            self.__url.update(url)

        @property
        def client_id(self):
            """
            :type: :class:`string`
            """
            return self.__client_id.value

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

        @property
        def url(self):
            """
            :type: :class:`string`
            """
            return self.__url.value

    def _initAttributes(self, app=_rcv.Absent, created_at=_rcv.Absent, id=_rcv.Absent, note=_rcv.Absent, note_url=_rcv.Absent, scopes=_rcv.Absent, token=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
        super(Authorization, self)._initAttributes(**kwds)
        self.__app = _rcv.Attribute("Authorization.app", _rcv.StructureConverter(self.Session, Authorization.Application), app)
        self.__created_at = _rcv.Attribute("Authorization.created_at", _rcv.DatetimeConverter, created_at)
        self.__id = _rcv.Attribute("Authorization.id", _rcv.IntConverter, id)
        self.__note = _rcv.Attribute("Authorization.note", _rcv.StringConverter, note)
        self.__note_url = _rcv.Attribute("Authorization.note_url", _rcv.StringConverter, note_url)
        self.__scopes = _rcv.Attribute("Authorization.scopes", _rcv.ListConverter(_rcv.StringConverter), scopes)
        self.__token = _rcv.Attribute("Authorization.token", _rcv.StringConverter, token)
        self.__updated_at = _rcv.Attribute("Authorization.updated_at", _rcv.DatetimeConverter, updated_at)

    def _updateAttributes(self, eTag, app=_rcv.Absent, created_at=_rcv.Absent, id=_rcv.Absent, note=_rcv.Absent, note_url=_rcv.Absent, scopes=_rcv.Absent, token=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
        super(Authorization, self)._updateAttributes(eTag, **kwds)
        self.__app.update(app)
        self.__created_at.update(created_at)
        self.__id.update(id)
        self.__note.update(note)
        self.__note_url.update(note_url)
        self.__scopes.update(scopes)
        self.__token.update(token)
        self.__updated_at.update(updated_at)

    @property
    def app(self):
        """
        :type: :class:`.Authorization.Application`
        """
        self._completeLazily(self.__app.needsLazyCompletion)
        return self.__app.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def note(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__note.needsLazyCompletion)
        return self.__note.value

    @property
    def note_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__note_url.needsLazyCompletion)
        return self.__note_url.value

    @property
    def scopes(self):
        """
        :type: :class:`list` of :class:`string`
        """
        self._completeLazily(self.__scopes.needsLazyCompletion)
        return self.__scopes.value

    @property
    def token(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__token.needsLazyCompletion)
        return self.__token.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    def delete(self):
        """
        Calls the `DELETE /authorizations/:id <http://developer.github.com/v3/oauth_authorizations#delete-an-authorization>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)

    def edit(self, scopes=None, add_scopes=None, remove_scopes=None, note=None, note_url=None):
        """
        Calls the `PATCH /authorizations/:id <http://developer.github.com/v3/oauth_authorizations#update-an-existing-authorization>`__ end point.

        This is the only method calling this end point.

        :param scopes: optional :class:`list` of :class:`string`
        :param add_scopes: optional :class:`list` of :class:`string`
        :param remove_scopes: optional :class:`list` of :class:`string`
        :param note: optional :class:`string`
        :param note_url: optional :class:`string` or :class:`Reset`
        :rtype: None
        """

        if scopes is not None:
            scopes = _snd.normalizeList(_snd.normalizeString, scopes)
        if add_scopes is not None:
            add_scopes = _snd.normalizeList(_snd.normalizeString, add_scopes)
        if remove_scopes is not None:
            remove_scopes = _snd.normalizeList(_snd.normalizeString, remove_scopes)
        if note is not None:
            note = _snd.normalizeString(note)
        if note_url is not None:
            note_url = _snd.normalizeStringReset(note_url)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(add_scopes=add_scopes, note=note, note_url=note_url, remove_scopes=remove_scopes, scopes=scopes)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())
