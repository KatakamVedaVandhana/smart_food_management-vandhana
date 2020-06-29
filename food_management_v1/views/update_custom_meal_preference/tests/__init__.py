# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "update_custom_meal_preference"
REQUEST_METHOD = "put"
URL_SUFFIX = "meal/custom_meal/update/v1/"

from .test_case_01 import TestCase01UpdateCustomMealPreferenceAPITestCase

__all__ = [
    "TestCase01UpdateCustomMealPreferenceAPITestCase"
]
