from django.db import models
from food_management.models.meal import Meal
from food_management.models.user import User
from food_management.models.items import Items
from food_management.constants.enums import RatingType


class UserRating(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    item = models.ForeignKey('Items', on_delete=models.CASCADE)
    quality = models.IntegerField(
        choices=RatingType.get_list_of_tuples(), default=0
    )
    taste = models.IntegerField(
        choices=RatingType.get_list_of_tuples(), default=0
    )
