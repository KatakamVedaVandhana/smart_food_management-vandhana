# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03LoginPageAPITestCase::test_case status'] = 200

snapshots['TestCase03LoginPageAPITestCase::test_case body'] = {
    'access_token': 'QyP8ahj39V26URvC9Jf73KXrdxdHbG',
    'expires_in': '2052-03-09 23:32:19.379768',
    'is_admin': False,
    'refresh_token': 'VOFldUZmQrpZFhqRE9JqNQZGaqDo9D',
    'user_id': 1
}

snapshots['TestCase03LoginPageAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '178',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}

snapshots['TestCase03LoginPageAPITestCase::test_case username'] = 'username_1'

snapshots['TestCase03LoginPageAPITestCase::test_case password'] = 'pbkdf2_sha256$150000$B27n1O07Apdr$9bk1+EDzy2kxfo0ABR/W1bUjCuXu0XuMrwbbOJWp6g4='
