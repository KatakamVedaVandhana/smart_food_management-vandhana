# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateUserMealPreferenceAPITestCase::test_case status'] = 200

snapshots['TestCase02UpdateUserMealPreferenceAPITestCase::test_case body'] = b''

snapshots['TestCase02UpdateUserMealPreferenceAPITestCase::test_case header_params'] = {
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

snapshots['TestCase02UpdateUserMealPreferenceAPITestCase::test_case meal_course'] = GenericRepr("<QuerySet [{'meal_course__meal_course': 'Half-meal'}, {'meal_course__meal_course': 'Half-meal'}, {'meal_course__meal_course': 'Half-meal'}]>")
