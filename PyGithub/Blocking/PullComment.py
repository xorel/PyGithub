# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class PullComment(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.PullRequest.create_pull_comment`
      * :meth:`.PullRequest.get_pull_comments`
      * :meth:`.Repository.get_pull_comment`
      * :meth:`.Repository.get_pull_comments`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, body=_rcv.Absent, body_html=_rcv.Absent, body_text=_rcv.Absent, commit_id=_rcv.Absent, created_at=_rcv.Absent, diff_hunk=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, original_commit_id=_rcv.Absent, original_position=_rcv.Absent, path=_rcv.Absent, position=_rcv.Absent, pull_request_url=_rcv.Absent, updated_at=_rcv.Absent, user=_rcv.Absent, _links=None, **kwds):
        import PyGithub.Blocking.User
        super(PullComment, self)._initAttributes(**kwds)
        self.__body = _rcv.Attribute("PullComment.body", _rcv.StringConverter, body)
        self.__body_html = _rcv.Attribute("PullComment.body_html", _rcv.StringConverter, body_html)
        self.__body_text = _rcv.Attribute("PullComment.body_text", _rcv.StringConverter, body_text)
        self.__commit_id = _rcv.Attribute("PullComment.commit_id", _rcv.StringConverter, commit_id)
        self.__created_at = _rcv.Attribute("PullComment.created_at", _rcv.DatetimeConverter, created_at)
        self.__diff_hunk = _rcv.Attribute("PullComment.diff_hunk", _rcv.StringConverter, diff_hunk)
        self.__html_url = _rcv.Attribute("PullComment.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("PullComment.id", _rcv.IntConverter, id)
        self.__original_commit_id = _rcv.Attribute("PullComment.original_commit_id", _rcv.StringConverter, original_commit_id)
        self.__original_position = _rcv.Attribute("PullComment.original_position", _rcv.IntConverter, original_position)
        self.__path = _rcv.Attribute("PullComment.path", _rcv.StringConverter, path)
        self.__position = _rcv.Attribute("PullComment.position", _rcv.IntConverter, position)
        self.__pull_request_url = _rcv.Attribute("PullComment.pull_request_url", _rcv.StringConverter, pull_request_url)
        self.__updated_at = _rcv.Attribute("PullComment.updated_at", _rcv.DatetimeConverter, updated_at)
        self.__user = _rcv.Attribute("PullComment.user", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)

    def _updateAttributes(self, eTag, body=_rcv.Absent, body_html=_rcv.Absent, body_text=_rcv.Absent, commit_id=_rcv.Absent, created_at=_rcv.Absent, diff_hunk=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, original_commit_id=_rcv.Absent, original_position=_rcv.Absent, path=_rcv.Absent, position=_rcv.Absent, pull_request_url=_rcv.Absent, updated_at=_rcv.Absent, user=_rcv.Absent, _links=None, **kwds):
        super(PullComment, self)._updateAttributes(eTag, **kwds)
        self.__body.update(body)
        self.__body_html.update(body_html)
        self.__body_text.update(body_text)
        self.__commit_id.update(commit_id)
        self.__created_at.update(created_at)
        self.__diff_hunk.update(diff_hunk)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__original_commit_id.update(original_commit_id)
        self.__original_position.update(original_position)
        self.__path.update(path)
        self.__position.update(position)
        self.__pull_request_url.update(pull_request_url)
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
    def commit_id(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__commit_id.needsLazyCompletion)
        return self.__commit_id.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def diff_hunk(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__diff_hunk.needsLazyCompletion)
        return self.__diff_hunk.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def original_commit_id(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__original_commit_id.needsLazyCompletion)
        return self.__original_commit_id.value

    @property
    def original_position(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__original_position.needsLazyCompletion)
        return self.__original_position.value

    @property
    def path(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__path.needsLazyCompletion)
        return self.__path.value

    @property
    def position(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__position.needsLazyCompletion)
        return self.__position.value

    @property
    def pull_request_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__pull_request_url.needsLazyCompletion)
        return self.__pull_request_url.value

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
        Calls the `DELETE /repos/:owner/:repo/pulls/comments/:number <http://developer.github.com/v3/pulls/comments#delete-a-comment>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self._url)
        r = self.Session._request("DELETE", url)

    def edit(self, body):
        """
        Calls the `PATCH /repos/:owner/:repo/pulls/comments/:number <http://developer.github.com/v3/pulls/comments#edit-a-comment>`__ end point.

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
