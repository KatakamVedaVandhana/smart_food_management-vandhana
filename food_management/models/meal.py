from django.db import models
from food_management.models import Items
from food_management.constants.enums import TypeOfMeal

class Meal(models.Model):
    item = models.ManyToManyField('Items', through='MealCourse')
    meal_type = models.CharField(
        choices=TypeOfMeal.get_list_of_tuples(), max_length=200,
        null=False
    )
    from_time_string = models.TimeField()
    to_time_string = models.TimeField()
    date = models.DateField()
