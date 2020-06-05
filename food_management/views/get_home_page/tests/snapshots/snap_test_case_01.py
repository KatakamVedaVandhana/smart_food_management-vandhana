# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetHomePageAPITestCase::test_case status'] = 200

snapshots['TestCase01GetHomePageAPITestCase::test_case body'] = [
    {
        'from_datetime_string': 'string',
        'items': [
            {
                'id': 1,
                'meal_item': 'string',
                'units': 'pieces'
            }
        ],
        'meal_course': 'half-meal',
        'meal_type': 'Breakfast',
        'to_datetime_string': 'string'
    }
]
