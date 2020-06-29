from django.db import models
from food_management.models import User
from food_management.constants.enums import CategoryType, CourseType
from food_management.models.meal_course import MealCourse
from food_management.models.meal import Meal
from food_management.models.items import Items


class UserMealStatus(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    custom_meal_quantity = models.IntegerField(default=0)
    item = models.ForeignKey('Items', on_delete=models.CASCADE, null=True)
    meal_course = models.ForeignKey('MealCourse', on_delete=models.CASCADE)
    # meal_course = models.CharField(
    #     choices = CourseType.get_list_of_tuples(), max_length=200
    # )
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)