from django.db import models
from food_management.constants.enums import BaseUnitType
from food_management.models import Meal, Items

class FoodWastage(models.Model):
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    item = models.ForeignKey('Items', on_delete=models.CASCADE)
    food_wasted= models.IntegerField()
    food_prepared = models.IntegerField()
    base_unit = models.CharField(
        choices=BaseUnitType.get_list_of_tuples(), max_length=100
    )
