# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime
import logging

import PyGithub.Blocking.tests.Framework as Framework

# @todoAlpha Test those messages as unit tests in SessionTestCases.py (when we have a SessionTestCases.py...)


# class DebugMessagesTestCase(Framework.SimpleLoginTestCase):
#     def testSimpleRequest(self):
#         logging.getLogger("PyGithub").setLevel(logging.DEBUG)
#         self.expectLog(
#             logging.DEBUG,
#             """GET https://api.github.com/users/jacquev6 [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('Authorization', 'Basic not_logged'), ('User-Agent', 'jacquev6/PyGithub/2; UnitTests recorder')] None => 200 [(u'access-control-allow-credentials', u'true'), (u'access-control-allow-origin', u'*'), (u'access-control-expose-headers', u'ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval'), (u'cache-control', u'private, max-age=60, s-maxage=60'), (u'content-encoding', u'gzip'), (u'content-type', u'application/json; charset=utf-8'), (u'date', u'Sun, 22 Dec 2013 19:20:02 GMT'), (u'etag', u'"0045423fc06bf81883739f7766565784"'), (u'last-modified', u'Sun, 22 Dec 2013 10:58:06 GMT'), (u'server', u'GitHub.com'), (u'status', u'200 OK'), (u'transfer-encoding', u'chunked'), (u'vary', u'Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding'), (u'x-content-type-options', u'nosniff'), (u'x-github-media-type', u'github.v3; param=full; format=json'), (u'x-github-request-id', u'4C79374B:32C8:1DA33F9:52B73B62'), (u'x-ratelimit-limit', u'5000'), (u'x-ratelimit-remaining', u'4959'), (u'x-ratelimit-reset', u'1387741483')] {"avatar_url": "https://gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https%3A%2F%2Fidenticons.github.com%2Ffadfb5f7088ef66579d198a3c9a4935e.png&r=x", "bio": null, "blog": "http://vincent-jacques.net", "collaborators": 0, "company": "Amazon", "created_at": "2010-07-09T06:10:06Z", "disk_usage": 91985, "email": "vincent@vincent-jacques.net", "events_url": "https://api.github.com/users/jacquev6/events{/privacy}", "followers": 30, "followers_url": "https://api.github.com/users/jacquev6/followers", "following": 43, "following_url": "https://api.github.com/users/jacquev6/following{/other_user}", "gists_url": "https://api.github.com/users/jacquev6/gists{/gist_id}", "gravatar_id": "b68de5ae38616c296fa345d2b9df2225", "hireable": false, "html_url": "https://github.com/jacquev6", "id": 327146, "location": "Seattle, WA, United States", "login": "jacquev6", "name": "Vincent Jacques", "organizations_url": "https://api.github.com/users/jacquev6/orgs", "owned_private_repos": 3, "plan": {"collaborators": 1, "name": "micro", "private_repos": 5, "space": 614400}, "private_gists": 6, "public_gists": 5, "public_repos": 19, "received_events_url": "https://api.github.com/users/jacquev6/received_events", "repos_url": "https://api.github.com/users/jacquev6/repos", "site_admin": false, "starred_url": "https://api.github.com/users/jacquev6/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/jacquev6/subscriptions", "total_private_repos": 3, "type": "User", "updated_at": "2013-12-22T10:58:06Z", "url": "https://api.github.com/users/jacquev6"}""",
#             """GET https://api.github.com/users/jacquev6 [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('Authorization', 'Basic not_logged'), ('User-Agent', 'jacquev6/PyGithub/2; UnitTests recorder')] None => 200 [('access-control-allow-credentials', 'true'), ('access-control-allow-origin', '*'), ('access-control-expose-headers', 'ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval'), ('cache-control', 'private, max-age=60, s-maxage=60'), ('content-encoding', 'gzip'), ('content-type', 'application/json; charset=utf-8'), ('date', 'Sun, 22 Dec 2013 19:20:02 GMT'), ('etag', '"0045423fc06bf81883739f7766565784"'), ('last-modified', 'Sun, 22 Dec 2013 10:58:06 GMT'), ('server', 'GitHub.com'), ('status', '200 OK'), ('transfer-encoding', 'chunked'), ('vary', 'Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding'), ('x-content-type-options', 'nosniff'), ('x-github-media-type', 'github.v3; param=full; format=json'), ('x-github-request-id', '4C79374B:32C8:1DA33F9:52B73B62'), ('x-ratelimit-limit', '5000'), ('x-ratelimit-remaining', '4959'), ('x-ratelimit-reset', '1387741483')] {"avatar_url": "https://gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https%3A%2F%2Fidenticons.github.com%2Ffadfb5f7088ef66579d198a3c9a4935e.png&r=x", "bio": null, "blog": "http://vincent-jacques.net", "collaborators": 0, "company": "Amazon", "created_at": "2010-07-09T06:10:06Z", "disk_usage": 91985, "email": "vincent@vincent-jacques.net", "events_url": "https://api.github.com/users/jacquev6/events{/privacy}", "followers": 30, "followers_url": "https://api.github.com/users/jacquev6/followers", "following": 43, "following_url": "https://api.github.com/users/jacquev6/following{/other_user}", "gists_url": "https://api.github.com/users/jacquev6/gists{/gist_id}", "gravatar_id": "b68de5ae38616c296fa345d2b9df2225", "hireable": false, "html_url": "https://github.com/jacquev6", "id": 327146, "location": "Seattle, WA, United States", "login": "jacquev6", "name": "Vincent Jacques", "organizations_url": "https://api.github.com/users/jacquev6/orgs", "owned_private_repos": 3, "plan": {"collaborators": 1, "name": "micro", "private_repos": 5, "space": 614400}, "private_gists": 6, "public_gists": 5, "public_repos": 19, "received_events_url": "https://api.github.com/users/jacquev6/received_events", "repos_url": "https://api.github.com/users/jacquev6/repos", "site_admin": false, "starred_url": "https://api.github.com/users/jacquev6/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/jacquev6/subscriptions", "total_private_repos": 3, "type": "User", "updated_at": "2013-12-22T10:58:06Z", "url": "https://api.github.com/users/jacquev6"}""",
#         )
#         self.g.get_user("jacquev6")


# class DebugMessagesAnonymousTestCase(Framework.SimpleAnonymousTestCase):
#     def testSimpleRequest(self):
#         logging.getLogger("PyGithub").setLevel(logging.DEBUG)
#         self.expectLog(
#             logging.DEBUG,
#             """GET https://api.github.com/users/jacquev6 [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('User-Agent', 'jacquev6/PyGithub/2; UnitTests recorder')] None => 200 [(u'access-control-allow-credentials', u'true'), (u'access-control-allow-origin', u'*'), (u'access-control-expose-headers', u'ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval'), (u'cache-control', u'public, max-age=60, s-maxage=60'), (u'content-encoding', u'gzip'), (u'content-type', u'application/json; charset=utf-8'), (u'date', u'Sun, 22 Dec 2013 19:48:37 GMT'), (u'etag', u'"cf5f68a57f0953e9fb65b39efb6f29d0"'), (u'last-modified', u'Sun, 22 Dec 2013 10:58:06 GMT'), (u'server', u'GitHub.com'), (u'status', u'200 OK'), (u'transfer-encoding', u'chunked'), (u'vary', u'Accept, Accept-Encoding'), (u'x-content-type-options', u'nosniff'), (u'x-github-media-type', u'github.v3; param=full; format=json'), (u'x-github-request-id', u'4C79374B:2B97:1E82688:52B74215'), (u'x-ratelimit-limit', u'60'), (u'x-ratelimit-remaining', u'57'), (u'x-ratelimit-reset', u'1387745126')] {"avatar_url": "https://gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https%3A%2F%2Fidenticons.github.com%2Ffadfb5f7088ef66579d198a3c9a4935e.png&r=x", "bio": null, "blog": "http://vincent-jacques.net", "company": "Amazon", "created_at": "2010-07-09T06:10:06Z", "email": "vincent@vincent-jacques.net", "events_url": "https://api.github.com/users/jacquev6/events{/privacy}", "followers": 30, "followers_url": "https://api.github.com/users/jacquev6/followers", "following": 43, "following_url": "https://api.github.com/users/jacquev6/following{/other_user}", "gists_url": "https://api.github.com/users/jacquev6/gists{/gist_id}", "gravatar_id": "b68de5ae38616c296fa345d2b9df2225", "hireable": false, "html_url": "https://github.com/jacquev6", "id": 327146, "location": "Seattle, WA, United States", "login": "jacquev6", "name": "Vincent Jacques", "organizations_url": "https://api.github.com/users/jacquev6/orgs", "public_gists": 5, "public_repos": 19, "received_events_url": "https://api.github.com/users/jacquev6/received_events", "repos_url": "https://api.github.com/users/jacquev6/repos", "site_admin": false, "starred_url": "https://api.github.com/users/jacquev6/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/jacquev6/subscriptions", "type": "User", "updated_at": "2013-12-22T10:58:06Z", "url": "https://api.github.com/users/jacquev6"}""",
#             """GET https://api.github.com/users/jacquev6 [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('User-Agent', 'jacquev6/PyGithub/2; UnitTests recorder')] None => 200 [('access-control-allow-credentials', 'true'), ('access-control-allow-origin', '*'), ('access-control-expose-headers', 'ETag, Link, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval'), ('cache-control', 'public, max-age=60, s-maxage=60'), ('content-encoding', 'gzip'), ('content-type', 'application/json; charset=utf-8'), ('date', 'Sun, 22 Dec 2013 19:48:37 GMT'), ('etag', '"cf5f68a57f0953e9fb65b39efb6f29d0"'), ('last-modified', 'Sun, 22 Dec 2013 10:58:06 GMT'), ('server', 'GitHub.com'), ('status', '200 OK'), ('transfer-encoding', 'chunked'), ('vary', 'Accept, Accept-Encoding'), ('x-content-type-options', 'nosniff'), ('x-github-media-type', 'github.v3; param=full; format=json'), ('x-github-request-id', '4C79374B:2B97:1E82688:52B74215'), ('x-ratelimit-limit', '60'), ('x-ratelimit-remaining', '57'), ('x-ratelimit-reset', '1387745126')] {"avatar_url": "https://gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https%3A%2F%2Fidenticons.github.com%2Ffadfb5f7088ef66579d198a3c9a4935e.png&r=x", "bio": null, "blog": "http://vincent-jacques.net", "company": "Amazon", "created_at": "2010-07-09T06:10:06Z", "email": "vincent@vincent-jacques.net", "events_url": "https://api.github.com/users/jacquev6/events{/privacy}", "followers": 30, "followers_url": "https://api.github.com/users/jacquev6/followers", "following": 43, "following_url": "https://api.github.com/users/jacquev6/following{/other_user}", "gists_url": "https://api.github.com/users/jacquev6/gists{/gist_id}", "gravatar_id": "b68de5ae38616c296fa345d2b9df2225", "hireable": false, "html_url": "https://github.com/jacquev6", "id": 327146, "location": "Seattle, WA, United States", "login": "jacquev6", "name": "Vincent Jacques", "organizations_url": "https://api.github.com/users/jacquev6/orgs", "public_gists": 5, "public_repos": 19, "received_events_url": "https://api.github.com/users/jacquev6/received_events", "repos_url": "https://api.github.com/users/jacquev6/repos", "site_admin": false, "starred_url": "https://api.github.com/users/jacquev6/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/jacquev6/subscriptions", "type": "User", "updated_at": "2013-12-22T10:58:06Z", "url": "https://api.github.com/users/jacquev6"}""",
#         )
#         self.g.get_user("jacquev6")


# class DebugMessagesOAuthTestCase(Framework.SimpleOAuthWithoutScopesTestCase):
#     def testSimpleRequest(self):
#         logging.getLogger("PyGithub").setLevel(logging.DEBUG)
#         self.expectLog(
#             logging.DEBUG,
#             """GET https://api.github.com/users/jacquev6 [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('Authorization', 'token not_logged'), ('User-Agent', 'jacquev6/PyGithub/2; UnitTests recorder')] None => 200 [(u'access-control-allow-credentials', u'true'), (u'access-control-allow-origin', u'*'), (u'access-control-expose-headers', u'ETag, Link, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval'), (u'cache-control', u'private, max-age=60, s-maxage=60'), (u'content-encoding', u'gzip'), (u'content-type', u'application/json; charset=utf-8'), (u'date', u'Thu, 27 Feb 2014 02:18:16 GMT'), (u'etag', u'"c1affdda34875705347252bbd1058f3f"'), (u'last-modified', u'Wed, 26 Feb 2014 21:15:44 GMT'), (u'server', u'GitHub.com'), (u'status', u'200 OK'), (u'transfer-encoding', u'chunked'), (u'vary', u'Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding'), (u'x-accepted-oauth-scopes', u''), (u'x-content-type-options', u'nosniff'), (u'x-github-media-type', u'github.v3; param=full; format=json'), (u'x-github-request-id', u'62E81E32:4AD1:2DBA00:530EA068'), (u'x-oauth-scopes', u''), (u'x-ratelimit-limit', u'12500'), (u'x-ratelimit-remaining', u'12431'), (u'x-ratelimit-reset', u'1393468234')] {"avatar_url": "https://avatars.githubusercontent.com/u/327146", "bio": null, "blog": "http://vincent-jacques.net", "company": "Amazon", "created_at": "2010-07-09T06:10:06Z", "email": "vincent@vincent-jacques.net", "events_url": "https://api.github.com/users/jacquev6/events{/privacy}", "followers": 30, "followers_url": "https://api.github.com/users/jacquev6/followers", "following": 44, "following_url": "https://api.github.com/users/jacquev6/following{/other_user}", "gists_url": "https://api.github.com/users/jacquev6/gists{/gist_id}", "gravatar_id": "b68de5ae38616c296fa345d2b9df2225", "hireable": false, "html_url": "https://github.com/jacquev6", "id": 327146, "location": "Seattle, WA, United States", "login": "jacquev6", "name": "Vincent Jacques", "organizations_url": "https://api.github.com/users/jacquev6/orgs", "public_gists": 5, "public_repos": 21, "received_events_url": "https://api.github.com/users/jacquev6/received_events", "repos_url": "https://api.github.com/users/jacquev6/repos", "site_admin": false, "starred_url": "https://api.github.com/users/jacquev6/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/jacquev6/subscriptions", "type": "User", "updated_at": "2014-02-26T21:15:44Z", "url": "https://api.github.com/users/jacquev6"}""",
#             """GET https://api.github.com/users/jacquev6 [('Accept', 'application/vnd.github.v3.full+json'), ('Accept-Encoding', 'gzip, deflate, compress'), ('Authorization', 'token not_logged'), ('User-Agent', 'jacquev6/PyGithub/2; UnitTests recorder')] None => 200 [('access-control-allow-credentials', 'true'), ('access-control-allow-origin', '*'), ('access-control-expose-headers', 'ETag, Link, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval'), ('cache-control', 'private, max-age=60, s-maxage=60'), ('content-encoding', 'gzip'), ('content-type', 'application/json; charset=utf-8'), ('date', 'Thu, 27 Feb 2014 02:18:16 GMT'), ('etag', '"c1affdda34875705347252bbd1058f3f"'), ('last-modified', 'Wed, 26 Feb 2014 21:15:44 GMT'), ('server', 'GitHub.com'), ('status', '200 OK'), ('transfer-encoding', 'chunked'), ('vary', 'Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding'), ('x-accepted-oauth-scopes', ''), ('x-content-type-options', 'nosniff'), ('x-github-media-type', 'github.v3; param=full; format=json'), ('x-github-request-id', '62E81E32:4AD1:2DBA00:530EA068'), ('x-oauth-scopes', ''), ('x-ratelimit-limit', '12500'), ('x-ratelimit-remaining', '12431'), ('x-ratelimit-reset', '1393468234')] {"avatar_url": "https://avatars.githubusercontent.com/u/327146", "bio": null, "blog": "http://vincent-jacques.net", "company": "Amazon", "created_at": "2010-07-09T06:10:06Z", "email": "vincent@vincent-jacques.net", "events_url": "https://api.github.com/users/jacquev6/events{/privacy}", "followers": 30, "followers_url": "https://api.github.com/users/jacquev6/followers", "following": 44, "following_url": "https://api.github.com/users/jacquev6/following{/other_user}", "gists_url": "https://api.github.com/users/jacquev6/gists{/gist_id}", "gravatar_id": "b68de5ae38616c296fa345d2b9df2225", "hireable": false, "html_url": "https://github.com/jacquev6", "id": 327146, "location": "Seattle, WA, United States", "login": "jacquev6", "name": "Vincent Jacques", "organizations_url": "https://api.github.com/users/jacquev6/orgs", "public_gists": 5, "public_repos": 21, "received_events_url": "https://api.github.com/users/jacquev6/received_events", "repos_url": "https://api.github.com/users/jacquev6/repos", "site_admin": false, "starred_url": "https://api.github.com/users/jacquev6/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/jacquev6/subscriptions", "type": "User", "updated_at": "2014-02-26T21:15:44Z", "url": "https://api.github.com/users/jacquev6"}""",
#         )
#         self.g.get_user("jacquev6")
