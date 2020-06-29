# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetUserRatingAPITestCase::test_case status'] = 200

snapshots['TestCase02GetUserRatingAPITestCase::test_case body'] = {
    'description': 'Nice',
    'items_and_ratings': [
        {
            'item_id': 1,
            'quality': 5,
            'taste': 4
        },
        {
            'item_id': 2,
            'quality': 1,
            'taste': 2
        },
        {
            'item_id': 3,
            'quality': 3,
            'taste': 4
        }
    ]
}

snapshots['TestCase02GetUserRatingAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '172',
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
