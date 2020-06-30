from food_management.models.items import Items
from food_management.models.announcements import Announcements
from food_management.models.user_rating import UserRating
from food_management.models.user_feedback import UserFeedback
from food_management.models.meal import Meal
from food_management.models.user_meal_status import UserMealStatus
from food_management.models.meal_course import MealCourse
from food_management.models.food_wastage import FoodWastage
#from food_management.models.user import User


__all__ = [
    "Items",
    "Announcements",
    "UserRating",
    "UserFeedback",
    "Meal",
    "UserMealStatus",
    "MealCourse",
    'FoodWastage'
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
