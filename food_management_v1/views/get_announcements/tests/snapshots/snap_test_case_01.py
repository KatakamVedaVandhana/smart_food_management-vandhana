# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAnnouncementsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetAnnouncementsAPITestCase::test_case body'] = [
    {
        'description': 'string',
        'image': 'string',
        'subtitle': 'festival_season',
        'title': 'announcement'
    }
]

snapshots['TestCase01GetAnnouncementsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '95',
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
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
