# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Release(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.create_release`
      * :meth:`.Repository.get_release`
      * :meth:`.Repository.get_releases`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, assets=_rcv.Absent, assets_url=_rcv.Absent, author=_rcv.Absent, body=_rcv.Absent, body_html=_rcv.Absent, body_text=_rcv.Absent, created_at=_rcv.Absent, draft=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, name=_rcv.Absent, prerelease=_rcv.Absent, published_at=_rcv.Absent, tag_name=_rcv.Absent, tarball_url=_rcv.Absent, target_commitish=_rcv.Absent, upload_url=_rcv.Absent, zipball_url=_rcv.Absent, **kwds):
        import PyGithub.Blocking.Asset
        import PyGithub.Blocking.User
        super(Release, self)._initAttributes(**kwds)
        self.__assets = _rcv.Attribute("Release.assets", _rcv.ListConverter(_rcv.ClassConverter(self.Session, PyGithub.Blocking.Asset.Asset)), assets)
        self.__assets_url = _rcv.Attribute("Release.assets_url", _rcv.StringConverter, assets_url)
        self.__author = _rcv.Attribute("Release.author", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), author)
        self.__body = _rcv.Attribute("Release.body", _rcv.StringConverter, body)
        self.__body_html = _rcv.Attribute("Release.body_html", _rcv.StringConverter, body_html)
        self.__body_text = _rcv.Attribute("Release.body_text", _rcv.StringConverter, body_text)
        self.__created_at = _rcv.Attribute("Release.created_at", _rcv.DatetimeConverter, created_at)
        self.__draft = _rcv.Attribute("Release.draft", _rcv.BoolConverter, draft)
        self.__html_url = _rcv.Attribute("Release.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("Release.id", _rcv.IntConverter, id)
        self.__name = _rcv.Attribute("Release.name", _rcv.StringConverter, name)
        self.__prerelease = _rcv.Attribute("Release.prerelease", _rcv.BoolConverter, prerelease)
        self.__published_at = _rcv.Attribute("Release.published_at", _rcv.DatetimeConverter, published_at)
        self.__tag_name = _rcv.Attribute("Release.tag_name", _rcv.StringConverter, tag_name)
        self.__tarball_url = _rcv.Attribute("Release.tarball_url", _rcv.StringConverter, tarball_url)
        self.__target_commitish = _rcv.Attribute("Release.target_commitish", _rcv.StringConverter, target_commitish)
        self.__upload_url = _rcv.Attribute("Release.upload_url", _rcv.StringConverter, upload_url)
        self.__zipball_url = _rcv.Attribute("Release.zipball_url", _rcv.StringConverter, zipball_url)

    def _updateAttributes(self, eTag, assets=_rcv.Absent, assets_url=_rcv.Absent, author=_rcv.Absent, body=_rcv.Absent, body_html=_rcv.Absent, body_text=_rcv.Absent, created_at=_rcv.Absent, draft=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, name=_rcv.Absent, prerelease=_rcv.Absent, published_at=_rcv.Absent, tag_name=_rcv.Absent, tarball_url=_rcv.Absent, target_commitish=_rcv.Absent, upload_url=_rcv.Absent, zipball_url=_rcv.Absent, **kwds):
        super(Release, self)._updateAttributes(eTag, **kwds)
        self.__assets.update(assets)
        self.__assets_url.update(assets_url)
        self.__author.update(author)
        self.__body.update(body)
        self.__body_html.update(body_html)
        self.__body_text.update(body_text)
        self.__created_at.update(created_at)
        self.__draft.update(draft)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__name.update(name)
        self.__prerelease.update(prerelease)
        self.__published_at.update(published_at)
        self.__tag_name.update(tag_name)
        self.__tarball_url.update(tarball_url)
        self.__target_commitish.update(target_commitish)
        self.__upload_url.update(upload_url)
        self.__zipball_url.update(zipball_url)

    @property
    def assets(self):
        """
        :type: :class:`list` of :class:`~.Asset.Asset`
        """
        self._completeLazily(self.__assets.needsLazyCompletion)
        return self.__assets.value

    @property
    def assets_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__assets_url.needsLazyCompletion)
        return self.__assets_url.value

    @property
    def author(self):
        """
        :type: :class:`~.User.User`
        """
        self._completeLazily(self.__author.needsLazyCompletion)
        return self.__author.value

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
    def draft(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__draft.needsLazyCompletion)
        return self.__draft.value

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
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def prerelease(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__prerelease.needsLazyCompletion)
        return self.__prerelease.value

    @property
    def published_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__published_at.needsLazyCompletion)
        return self.__published_at.value

    @property
    def tag_name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__tag_name.needsLazyCompletion)
        return self.__tag_name.value

    @property
    def tarball_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__tarball_url.needsLazyCompletion)
        return self.__tarball_url.value

    @property
    def target_commitish(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__target_commitish.needsLazyCompletion)
        return self.__target_commitish.value

    @property
    def upload_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__upload_url.needsLazyCompletion)
        return self.__upload_url.value

    @property
    def zipball_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__zipball_url.needsLazyCompletion)
        return self.__zipball_url.value

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo/releases/:id <http://developer.github.com/v3/repos/releases#delete-a-release>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)

    def edit(self, tag_name=None, target_commitish=None, name=None, body=None, draft=None, prerelease=None):
        """
        Calls the `PATCH /repos/:owner/:repo/releases/:id <http://developer.github.com/v3/repos/releases#edit-a-release>`__ end point.

        This is the only method calling this end point.

        :param tag_name: optional :class:`string`
        :param target_commitish: optional :class:`string`
        :param name: optional :class:`string`
        :param body: optional :class:`string`
        :param draft: optional :class:`bool`
        :param prerelease: optional :class:`bool`
        :rtype: None
        """

        if tag_name is not None:
            tag_name = _snd.normalizeString(tag_name)
        if target_commitish is not None:
            target_commitish = _snd.normalizeString(target_commitish)
        if name is not None:
            name = _snd.normalizeString(name)
        if body is not None:
            body = _snd.normalizeString(body)
        if draft is not None:
            draft = _snd.normalizeBool(draft)
        if prerelease is not None:
            prerelease = _snd.normalizeBool(prerelease)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(body=body, draft=draft, name=name, prerelease=prerelease, tag_name=tag_name, target_commitish=target_commitish)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_assets(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/releases/:id/assets <http://developer.github.com/v3/repos/releases#list-assets-for-a-release>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`~.Asset.Asset`
        """
        import PyGithub.Blocking.Asset

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.assets_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Asset.Asset))(None, r)

    def upload_asset(self, content_type, name, content):
        """
        Calls the `POST /repos/:owner/:repo/releases/:id/assets <https://developer.github.com/v3/repos/releases/#upload-a-release-asset>`__ end point.

        This is the only method calling this end point.

        :param content_type: mandatory :class:`string`
        :param name: mandatory :class:`string`
        :param content: mandatory :class:`string`
        :rtype: :class:`~.Asset.Asset`
        """
        import PyGithub.Blocking.Asset

        content_type = _snd.normalizeString(content_type)
        name = _snd.normalizeString(name)
        content = _snd.normalizeString(content)

        url = uritemplate.expand(self.upload_url)
        urlArguments = _snd.dictionary(name=name)
        postArguments = content
        headers = {"Content-Type": content_type}
        r = self.Session._request("POST", url, urlArguments=urlArguments, postArguments=postArguments, headers=headers)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Asset.Asset)(None, r.json(), r.headers.get("ETag"))
