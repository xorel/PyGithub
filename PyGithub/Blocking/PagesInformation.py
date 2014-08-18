# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class PagesInformation(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_pages`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, cname=_rcv.Absent, custom_404=_rcv.Absent, status=_rcv.Absent, **kwds):
        super(PagesInformation, self)._initAttributes(**kwds)
        self.__cname = _rcv.Attribute("PagesInformation.cname", _rcv.StringConverter, cname)
        self.__custom_404 = _rcv.Attribute("PagesInformation.custom_404", _rcv.BoolConverter, custom_404)
        self.__status = _rcv.Attribute("PagesInformation.status", _rcv.StringConverter, status)

    def _updateAttributes(self, eTag, cname=_rcv.Absent, custom_404=_rcv.Absent, status=_rcv.Absent, **kwds):
        super(PagesInformation, self)._updateAttributes(eTag, **kwds)
        self.__cname.update(cname)
        self.__custom_404.update(custom_404)
        self.__status.update(status)

    @property
    def cname(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__cname.needsLazyCompletion)
        return self.__cname.value

    @property
    def custom_404(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__custom_404.needsLazyCompletion)
        return self.__custom_404.value

    @property
    def status(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__status.needsLazyCompletion)
        return self.__status.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self._url

    def update(self):
        """
        Makes a `conditional request <http://developer.github.com/v3/#conditional-requests>`_ and updates the object.
        Returns True if the object was updated.

        :rtype: :class:`bool`
        """
        return self._update()
