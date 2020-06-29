# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03UpdateUserRatingAPITestCase::test_case status'] = 200

snapshots['TestCase03UpdateUserRatingAPITestCase::test_case body'] = b''

snapshots['TestCase03UpdateUserRatingAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '0',
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

snapshots['TestCase03UpdateUserRatingAPITestCase::test_case user_rating_obj_status'] = True

snapshots['TestCase03UpdateUserRatingAPITestCase::test_case user_feedback_obj_status'] = True
