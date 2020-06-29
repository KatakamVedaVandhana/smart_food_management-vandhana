# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateMealScheduleAPITestCase::test_case status'] = 400

snapshots['TestCase01UpdateMealScheduleAPITestCase::test_case body'] = {
    'date': [
        'This field is required.'
    ],
    'items_list': [
        {
            'non_field_errors': [
                'Invalid data. Expected a dictionary, but got int.'
            ]
        }
    ],
    'meal_type': [
        'This field is required.'
    ]
}

snapshots['TestCase01UpdateMealScheduleAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '166',
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
