# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetMealPreferenceAPITestCase::test_case status'] = 200

snapshots['TestCase03GetMealPreferenceAPITestCase::test_case body'] = [
    {
        'category': "('Indian-Bread', 'Indian-Bread')",
        'item': 'Idly',
        'item_id': 1,
        'meal_courses': [
            {
                'meal_course': 'Half-meal',
                'quantity': 3
            },
            {
                'meal_course': 'Full-meal',
                'quantity': 7
            },
            {
                'meal_course': 'Custom-meal',
                'quantity': 0
            },
            {
                'meal_course': 'Skip-meal',
                'quantity': 5
            }
        ],
        'units': "('pieces', 'pieces')"
    },
    {
        'category': "('Indian-Bread', 'Indian-Bread')",
        'item': 'Dosa',
        'item_id': 2,
        'meal_courses': [
            {
                'meal_course': 'Half-meal',
                'quantity': 4
            },
            {
                'meal_course': 'Full-meal',
                'quantity': 5
            },
            {
                'meal_course': 'Custom-meal',
                'quantity': 0
            },
            {
                'meal_course': 'Skip-meal',
                'quantity': 3
            }
        ],
        'units': "('pieces', 'pieces')"
    },
    {
        'category': "('Indian-Bread', 'Indian-Bread')",
        'item': 'Chutney',
        'item_id': 3,
        'meal_courses': [
            {
                'meal_course': 'Half-meal',
                'quantity': 2
            },
            {
                'meal_course': 'Full-meal',
                'quantity': 5
            },
            {
                'meal_course': 'Custom-meal',
                'quantity': 0
            },
            {
                'meal_course': 'Skip-meal',
                'quantity': 7
            }
        ],
        'units': "('pieces', 'pieces')"
    }
]

snapshots['TestCase03GetMealPreferenceAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '1820',
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
