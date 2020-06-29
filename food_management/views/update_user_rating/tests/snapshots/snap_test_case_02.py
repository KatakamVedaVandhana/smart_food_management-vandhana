# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateUserRatingAPITestCase::test_case status'] = 200

snapshots['TestCase02UpdateUserRatingAPITestCase::test_case body'] = b''

snapshots['TestCase02UpdateUserRatingAPITestCase::test_case header_params'] = {
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

snapshots['TestCase02UpdateUserRatingAPITestCase::test_case meal'] = GenericRepr("<QuerySet [{'meal': 1}, {'meal': 1}, {'meal': 1}]>")

snapshots['TestCase02UpdateUserRatingAPITestCase::test_case items'] = GenericRepr("<QuerySet [{'item': 1}, {'item': 2}, {'item': 3}]>")

snapshots['TestCase02UpdateUserRatingAPITestCase::test_case qualities'] = GenericRepr("<QuerySet [{'quality': 5}, {'quality': 5}, {'quality': 3}]>")

snapshots['TestCase02UpdateUserRatingAPITestCase::test_case tastes'] = GenericRepr("<QuerySet [{'taste': 5}, {'taste': 3}, {'taste': 3}]>")
