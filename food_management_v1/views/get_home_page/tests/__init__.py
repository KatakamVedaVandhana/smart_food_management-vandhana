# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "get_home_page"
REQUEST_METHOD = "post"
URL_SUFFIX = "home/v1/"

from .test_case_01 import TestCase01GetHomePageAPITestCase

__all__ = [
    "TestCase01GetHomePageAPITestCase"
]
