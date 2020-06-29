"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from food_management.utils.custom_utils import CustomTestUtils
from food_management.models.factories import MealFactory, ItemsFactory
from food_management.models import UserRating, UserFeedback, Meal

REQUEST_BODY = """
{
    "meal_type": "Breakfast",
    "date": "2020-02-12",
    "items_and_ratings": [
        {
            "item_id": 1,
            "quality": 5,
            "taste": 5
        },
        {
            "item_id": 2,
            "quality": 5,
            "taste": 3
        },
        {
            "item_id": 3,
            "quality": 3,
            "taste": 3
        }
    ],
    "description": "string"
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


class TestCase03UpdateUserRatingAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase03UpdateUserRatingAPITestCase, self).setupUser(
            username=username,
            password=password
        )
        self.get_meal_data_factory(meal_type='Breakfast', date='2020-02-12')

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        meal_obj = Meal.objects.get(meal_type='Breakfast', date='2020-02-12')
        user_rating_obj = UserRating.objects.filter(meal=meal_obj, user=self.foo_user).exists()
        user_feedback_obj = UserFeedback.objects.filter(meal=meal_obj, user=self.foo_user).exists()

        self.assert_match_snapshot(
            name='user_rating_obj_status',
            value=user_rating_obj
        )

        self.assert_match_snapshot(
            name='user_feedback_obj_status',
            value=user_feedback_obj
        )