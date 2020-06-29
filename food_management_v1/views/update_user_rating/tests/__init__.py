# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "update_user_rating"
REQUEST_METHOD = "post"
URL_SUFFIX = "rating/update/v1/"

from .test_case_01 import TestCase01UpdateUserRatingAPITestCase

__all__ = [
    "TestCase01UpdateUserRatingAPITestCase"
]
