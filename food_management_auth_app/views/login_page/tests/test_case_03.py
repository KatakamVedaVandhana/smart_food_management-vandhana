"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from food_management_auth_app.models.factories import UserFactory
from food_management_auth_app.models import User

REQUEST_BODY = """
{
    "username": "username_1",
    "password": "username_1"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase03LoginPageAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    def test_case(self):
        User.objects.create_user(username='username_1', password='username_1')
        user_obj = User.objects.get(id=1)
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

        self.assert_match_snapshot(
            name='username',
            value=user_obj.username
        )

        self.assert_match_snapshot(
            name='password',
            value=user_obj.password
        )
