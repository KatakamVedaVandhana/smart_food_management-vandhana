# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "get_meal_schedule"
REQUEST_METHOD = "post"
URL_SUFFIX = "admin/schedule_menu/v1/"

from .test_case_01 import TestCase01GetMealScheduleAPITestCase

__all__ = [
    "TestCase01GetMealScheduleAPITestCase"
]
