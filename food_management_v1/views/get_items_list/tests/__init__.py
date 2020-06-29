# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "get_items_list"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/schedule_menu/items_list/v1/"

from .test_case_01 import TestCase01GetItemsListAPITestCase

__all__ = [
    "TestCase01GetItemsListAPITestCase"
]
