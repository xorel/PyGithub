# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class IssueComment(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Issue.create_issue_comment`
      * :meth:`.Issue.get_issue_comments`
      * :meth:`.Repository.get_issue_comment`
      * :meth:`.Repository.get_issue_comments`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, body=_rcv.Absent, body_html=_rcv.Absent, body_text=_rcv.Absent, created_at=_rcv.Absent, id=_rcv.Absent, updated_at=_rcv.Absent, user=_rcv.Absent, **kwds):
        import PyGithub.Blocking.User
        super(IssueComment, self)._initAttributes(**kwds)
        self.__body = _rcv.Attribute("IssueComment.body", _rcv.StringConverter, body)
        self.__body_html = _rcv.Attribute("IssueComment.body_html", _rcv.StringConverter, body_html)
        self.__body_text = _rcv.Attribute("IssueComment.body_text", _rcv.StringConverter, body_text)
        self.__created_at = _rcv.Attribute("IssueComment.created_at", _rcv.DatetimeConverter, created_at)
        self.__id = _rcv.Attribute("IssueComment.id", _rcv.IntConverter, id)
        self.__updated_at = _rcv.Attribute("IssueComment.updated_at", _rcv.DatetimeConverter, updated_at)
        self.__user = _rcv.Attribute("IssueComment.user", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)

    def _updateAttributes(self, eTag, body=_rcv.Absent, body_html=_rcv.Absent, body_text=_rcv.Absent, created_at=_rcv.Absent, id=_rcv.Absent, updated_at=_rcv.Absent, user=_rcv.Absent, **kwds):
        super(IssueComment, self)._updateAttributes(eTag, **kwds)
        self.__body.update(body)
        self.__body_html.update(body_html)
        self.__body_text.update(body_text)
        self.__created_at.update(created_at)
        self.__id.update(id)
        self.__updated_at.update(updated_at)
        self.__user.update(user)

    @property
    def body(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__body.needsLazyCompletion)
        return self.__body.value

    @property
    def body_html(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__body_html.needsLazyCompletion)
        return self.__body_html.value

    @property
    def body_text(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__body_text.needsLazyCompletion)
        return self.__body_text.value

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
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    @property
    def user(self):
        """
        :type: :class:`~.User.User`
        """
        self._completeLazily(self.__user.needsLazyCompletion)
        return self.__user.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self._url

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo/issues/comments/:id <http://developer.github.com/v3/issues/comments#delete-a-comment>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self._url)
        r = self.Session._request("DELETE", url)

    def edit(self, body):
        """
        Calls the `PATCH /repos/:owner/:repo/issues/comments/:id <http://developer.github.com/v3/issues/comments#edit-a-comment>`__ end point.

        This is the only method calling this end point.

        :param body: mandatory :class:`string`
        :rtype: None
        """

        body = _snd.normalizeString(body)

        url = uritemplate.expand(self._url)
        postArguments = _snd.dictionary(body=body)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def update(self):
        """
        Makes a `conditional request <http://developer.github.com/v3/#conditional-requests>`_ and updates the object.
        Returns True if the object was updated.

        :rtype: :class:`bool`
        """
        return self._update()
