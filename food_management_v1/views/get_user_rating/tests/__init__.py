# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "get_user_rating"
REQUEST_METHOD = "post"
URL_SUFFIX = "rating/v1/"

from .test_case_01 import TestCase01GetUserRatingAPITestCase

__all__ = [
    "TestCase01GetUserRatingAPITestCase"
]
