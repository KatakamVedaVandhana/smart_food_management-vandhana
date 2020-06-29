# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetHomePageAPITestCase::test_case status'] = 200

snapshots['TestCase02GetHomePageAPITestCase::test_case body'] = [
    {
        'from_time_string': '07:00',
        'items': [
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'Idly',
                'item_id': 1,
                'units': "('pieces', 'pieces')"
            },
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'Dosa',
                'item_id': 2,
                'units': "('pieces', 'pieces')"
            },
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'Chutney',
                'item_id': 3,
                'units': "('pieces', 'pieces')"
            }
        ],
        'meal_course': 'Full-Meal',
        'meal_id': 1,
        'meal_type': 'Breakfast',
        'to_time_string': '10:00'
    },
    {
        'from_time_string': '07:00',
        'items': [
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'Rice',
                'item_id': 4,
                'units': "('pieces', 'pieces')"
            },
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'Brinjal',
                'item_id': 5,
                'units': "('pieces', 'pieces')"
            },
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'Curd',
                'item_id': 6,
                'units': "('pieces', 'pieces')"
            }
        ],
        'meal_course': 'Full-Meal',
        'meal_id': 2,
        'meal_type': 'Lunch',
        'to_time_string': '10:00'
    },
    {
        'from_time_string': '07:00',
        'items': [
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'Poori',
                'item_id': 7,
                'units': "('pieces', 'pieces')"
            },
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'PotatoCurry',
                'item_id': 8,
                'units': "('pieces', 'pieces')"
            },
            {
                'category': "('Indian-Bread', 'Indian-Bread')",
                'item': 'Roti',
                'item_id': 9,
                'units': "('pieces', 'pieces')"
            }
        ],
        'meal_course': 'Full-Meal',
        'meal_id': 3,
        'meal_type': 'Dinner',
        'to_time_string': '10:00'
    }
]

snapshots['TestCase02GetHomePageAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '2451',
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
