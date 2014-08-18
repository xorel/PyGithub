# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Asset(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Release.assets`
      * :meth:`.Release.get_assets`
      * :meth:`.Release.upload_asset`
      * :meth:`.Repository.get_release_asset`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, browser_download_url=_rcv.Absent, content_type=_rcv.Absent, created_at=_rcv.Absent, download_count=_rcv.Absent, id=_rcv.Absent, label=_rcv.Absent, name=_rcv.Absent, size=_rcv.Absent, state=_rcv.Absent, updated_at=_rcv.Absent, uploader=_rcv.Absent, **kwds):
        import PyGithub.Blocking.User
        super(Asset, self)._initAttributes(**kwds)
        self.__browser_download_url = _rcv.Attribute("Asset.browser_download_url", _rcv.StringConverter, browser_download_url)
        self.__content_type = _rcv.Attribute("Asset.content_type", _rcv.StringConverter, content_type)
        self.__created_at = _rcv.Attribute("Asset.created_at", _rcv.DatetimeConverter, created_at)
        self.__download_count = _rcv.Attribute("Asset.download_count", _rcv.IntConverter, download_count)
        self.__id = _rcv.Attribute("Asset.id", _rcv.IntConverter, id)
        self.__label = _rcv.Attribute("Asset.label", _rcv.StringConverter, label)
        self.__name = _rcv.Attribute("Asset.name", _rcv.StringConverter, name)
        self.__size = _rcv.Attribute("Asset.size", _rcv.IntConverter, size)
        self.__state = _rcv.Attribute("Asset.state", _rcv.StringConverter, state)
        self.__updated_at = _rcv.Attribute("Asset.updated_at", _rcv.DatetimeConverter, updated_at)
        self.__uploader = _rcv.Attribute("Asset.uploader", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), uploader)

    def _updateAttributes(self, eTag, browser_download_url=_rcv.Absent, content_type=_rcv.Absent, created_at=_rcv.Absent, download_count=_rcv.Absent, id=_rcv.Absent, label=_rcv.Absent, name=_rcv.Absent, size=_rcv.Absent, state=_rcv.Absent, updated_at=_rcv.Absent, uploader=_rcv.Absent, **kwds):
        super(Asset, self)._updateAttributes(eTag, **kwds)
        self.__browser_download_url.update(browser_download_url)
        self.__content_type.update(content_type)
        self.__created_at.update(created_at)
        self.__download_count.update(download_count)
        self.__id.update(id)
        self.__label.update(label)
        self.__name.update(name)
        self.__size.update(size)
        self.__state.update(state)
        self.__updated_at.update(updated_at)
        self.__uploader.update(uploader)

    @property
    def browser_download_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__browser_download_url.needsLazyCompletion)
        return self.__browser_download_url.value

    @property
    def content_type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__content_type.needsLazyCompletion)
        return self.__content_type.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def download_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__download_count.needsLazyCompletion)
        return self.__download_count.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def label(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__label.needsLazyCompletion)
        return self.__label.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def size(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__size.needsLazyCompletion)
        return self.__size.value

    @property
    def state(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__state.needsLazyCompletion)
        return self.__state.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    @property
    def uploader(self):
        """
        :type: :class:`~.User.User`
        """
        self._completeLazily(self.__uploader.needsLazyCompletion)
        return self.__uploader.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self._url

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo/releases/assets/:id <http://developer.github.com/v3/repos/releases#delete-a-release-asset>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self._url)
        r = self.Session._request("DELETE", url)

    def edit(self, name, label=None):
        """
        Calls the `PATCH /repos/:owner/:repo/releases/assets/:id <http://developer.github.com/v3/repos/releases#edit-a-release-asset>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :param label: optional :class:`string`
        :rtype: None
        """

        name = _snd.normalizeString(name)
        if label is not None:
            label = _snd.normalizeString(label)

        url = uritemplate.expand(self._url)
        postArguments = _snd.dictionary(label=label, name=name)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def update(self):
        """
        Makes a `conditional request <http://developer.github.com/v3/#conditional-requests>`_ and updates the object.
        Returns True if the object was updated.

        :rtype: :class:`bool`
        """
        return self._update()
