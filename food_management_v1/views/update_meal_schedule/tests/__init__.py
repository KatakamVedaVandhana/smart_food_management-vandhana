# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "update_meal_schedule"
REQUEST_METHOD = "put"
URL_SUFFIX = "admin/update_meal_schedule/v1/"

from .test_case_01 import TestCase01UpdateMealScheduleAPITestCase

__all__ = [
    "TestCase01UpdateMealScheduleAPITestCase"
]
