# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "get_meal_preference"
REQUEST_METHOD = "post"
URL_SUFFIX = "meal/preference/v1/"

from .test_case_01 import TestCase01GetMealPreferenceAPITestCase

__all__ = [
    "TestCase01GetMealPreferenceAPITestCase"
]
