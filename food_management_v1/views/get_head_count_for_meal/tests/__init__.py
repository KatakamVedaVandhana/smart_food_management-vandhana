# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "get_head_count_for_meal"
REQUEST_METHOD = "post"
URL_SUFFIX = "admin/head_counts/v1/"

from .test_case_01 import TestCase01GetHeadCountForMealAPITestCase

__all__ = [
    "TestCase01GetHeadCountForMealAPITestCase"
]
