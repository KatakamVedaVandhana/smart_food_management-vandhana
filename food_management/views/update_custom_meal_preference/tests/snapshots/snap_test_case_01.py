# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateCustomMealPreferenceAPITestCase::test_case status'] = 401

snapshots['TestCase01UpdateCustomMealPreferenceAPITestCase::test_case body'] = {
    'detail': 'Authentication credentials were not provided.'
}

snapshots['TestCase01UpdateCustomMealPreferenceAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '58',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'www-authenticate': [
        'Bearer realm="api"',
        'WWW-Authenticate'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
