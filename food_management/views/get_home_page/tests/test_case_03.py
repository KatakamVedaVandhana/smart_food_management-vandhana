"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from food_management.utils.custom_utils import CustomTestUtils

REQUEST_BODY = """
{"date": "2020-02-12"}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase03GetHomePageAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase03GetHomePageAPITestCase, self).setupUser(
            username=username,
            password=password
        )

        self.get_home_page_factories_with_user_meal_status(date='2020-02-12')

    def test_case(self):
        response = self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

        import json

        response_content = json.loads(response.content)
