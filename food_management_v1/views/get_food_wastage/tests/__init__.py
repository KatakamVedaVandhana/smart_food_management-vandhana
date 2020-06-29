# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "get_food_wastage"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/food_wastage/v1/"

from .test_case_01 import TestCase01GetFoodWastageAPITestCase

__all__ = [
    "TestCase01GetFoodWastageAPITestCase"
]
