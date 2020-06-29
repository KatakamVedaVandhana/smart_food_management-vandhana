# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_add_two_numbers_with_integer_values_as_input sum_of_two_integers'] = 3

snapshots['test_add_two_numbers_with_negative_values_as_input sum_of_two_negative_numbers'] = -4

snapshots['test_add_two_numbers_with_float_values_as_input sum_of_two_float_numbers'] = 4.7
