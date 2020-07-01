# pylint: disable=wrong-import-position

APP_NAME = "food_management_auth_app"
OPERATION_NAME = "login_page"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01LoginPageAPITestCase
from .test_case_02 import TestCase02LoginPageAPITestCase
from .test_case_03 import TestCase03LoginPageAPITestCase

__all__ = [
    "TestCase01LoginPageAPITestCase",
    "TestCase02LoginPageAPITestCase",
    "TestCase03LoginPageAPITestCase"
]
