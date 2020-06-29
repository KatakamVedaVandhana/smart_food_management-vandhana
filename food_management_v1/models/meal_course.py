from django.db import models
from food_management.constants.enums import CourseType
from food_management.models import Items
from food_management.models import Meal


class MealCourse(models.Model):
    item = models.ForeignKey('Items', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    meal_course = models.CharField(
        choices=CourseType.get_list_of_tuples(), max_length=200,
        null=False
    )
    quantity = models.IntegerField(default=0)