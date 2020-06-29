# pylint: disable=wrong-import-position

APP_NAME = "food_management"
OPERATION_NAME = "get_announcements"
REQUEST_METHOD = "get"
URL_SUFFIX = "announcements/v1/"

from .test_case_01 import TestCase01GetAnnouncementsAPITestCase

__all__ = [
    "TestCase01GetAnnouncementsAPITestCase"
]
