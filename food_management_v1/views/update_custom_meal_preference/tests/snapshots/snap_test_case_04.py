# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase04UpdateCustomMealPreferenceAPITestCase::test_case status'] = 200

snapshots['TestCase04UpdateCustomMealPreferenceAPITestCase::test_case body'] = b''

snapshots['TestCase04UpdateCustomMealPreferenceAPITestCase::test_case header_params'] = {
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

snapshots['TestCase04UpdateCustomMealPreferenceAPITestCase::test_case meal_course'] = GenericRepr("<QuerySet [{'meal_course__meal_course': 'Custom-meal'}, {'meal_course__meal_course': 'Custom-meal'}, {'meal_course__meal_course': 'Custom-meal'}]>")

snapshots['TestCase04UpdateCustomMealPreferenceAPITestCase::test_case quantity'] = GenericRepr("<QuerySet [{'custom_meal_quantity': 1}, {'custom_meal_quantity': 1}, {'custom_meal_quantity': 1}]>")

snapshots['TestCase04UpdateCustomMealPreferenceAPITestCase::test_case items'] = GenericRepr("<QuerySet [{'item__id': 1}, {'item__id': 2}, {'item__id': 3}]>")
