"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from food_management.utils.custom_utils import CustomTestUtils
from food_management.models import UserMealStatus, Meal

REQUEST_BODY = """
{
    "meal_type": "Breakfast",
    "meal_course": "Half-meal",
    "date": "2020-02-12"
}
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


class TestCase02UpdateUserMealPreferenceAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02UpdateUserMealPreferenceAPITestCase, self).setupUser(
            username=username,
            password=password
        )
        self.get_meal_data_factory(meal_type='Breakfast', date='2020-02-12')

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

        meal_obj = Meal.objects.get(meal_type='Breakfast', date='2020-02-12')
        user_meal_status_obj = UserMealStatus.objects.filter(meal=meal_obj, user=self.foo_user)

        self.assert_match_snapshot(
            name='meal_course',
            value=user_meal_status_obj.values('meal_course__meal_course')
        )
