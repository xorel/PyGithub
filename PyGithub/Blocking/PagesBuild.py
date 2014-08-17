# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class PagesBuild(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_latest_pages_build`
      * :meth:`.Repository.get_pages_builds`

    Methods accepting instances of this class as parameter: none.
    """

    class Error(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.PagesBuild.error`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, message=None, **kwds):
            super(PagesBuild.Error, self)._initAttributes(**kwds)
            self.__message = _rcv.Attribute("PagesBuild.Error.message", _rcv.StringConverter, message)

        def _updateAttributes(self, message=None, **kwds):
            super(PagesBuild.Error, self)._updateAttributes(**kwds)
            self.__message.update(message)

        @property
        def message(self):
            """
            :type: :class:`string`
            """
            return self.__message.value

    def _initAttributes(self, commit=_rcv.Absent, created_at=_rcv.Absent, duration=_rcv.Absent, error=_rcv.Absent, pusher=_rcv.Absent, status=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
        import PyGithub.Blocking.User
        super(PagesBuild, self)._initAttributes(**kwds)
        self.__commit = _rcv.Attribute("PagesBuild.commit", _rcv.StringConverter, commit)
        self.__created_at = _rcv.Attribute("PagesBuild.created_at", _rcv.DatetimeConverter, created_at)
        self.__duration = _rcv.Attribute("PagesBuild.duration", _rcv.IntConverter, duration)
        self.__error = _rcv.Attribute("PagesBuild.error", _rcv.StructureConverter(self.Session, PagesBuild.Error), error)
        self.__pusher = _rcv.Attribute("PagesBuild.pusher", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), pusher)
        self.__status = _rcv.Attribute("PagesBuild.status", _rcv.StringConverter, status)
        self.__updated_at = _rcv.Attribute("PagesBuild.updated_at", _rcv.DatetimeConverter, updated_at)

    def _updateAttributes(self, eTag, commit=_rcv.Absent, created_at=_rcv.Absent, duration=_rcv.Absent, error=_rcv.Absent, pusher=_rcv.Absent, status=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
        super(PagesBuild, self)._updateAttributes(eTag, **kwds)
        self.__commit.update(commit)
        self.__created_at.update(created_at)
        self.__duration.update(duration)
        self.__error.update(error)
        self.__pusher.update(pusher)
        self.__status.update(status)
        self.__updated_at.update(updated_at)

    @property
    def commit(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__commit.needsLazyCompletion)
        return self.__commit.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def duration(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__duration.needsLazyCompletion)
        return self.__duration.value

    @property
    def error(self):
        """
        :type: :class:`.PagesBuild.Error`
        """
        self._completeLazily(self.__error.needsLazyCompletion)
        return self.__error.value

    @property
    def pusher(self):
        """
        :type: :class:`~.User.User`
        """
        self._completeLazily(self.__pusher.needsLazyCompletion)
        return self.__pusher.value

    @property
    def status(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__status.needsLazyCompletion)
        return self.__status.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value
