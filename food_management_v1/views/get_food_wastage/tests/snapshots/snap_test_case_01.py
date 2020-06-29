# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetFoodWastageAPITestCase::test_case status'] = 400

snapshots['TestCase01GetFoodWastageAPITestCase::test_case body'] = {
    'date': [
        'This field is required.'
    ],
    'meal_type': [
        'This field is required.'
    ]
}

snapshots['TestCase01GetFoodWastageAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '76',
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
