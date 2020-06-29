# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "update_user_meal_preference"
REQUEST_METHOD = "put"
URL_SUFFIX = "meal/preference/update/v1/"

from .test_case_01 import TestCase01UpdateUserMealPreferenceAPITestCase

__all__ = [
    "TestCase01UpdateUserMealPreferenceAPITestCase"
]
