from django.db import models
from food_management.constants.enums import CategoryType
from food_management.constants.enums import UnitType

class Items(models.Model):
    item = models.CharField(max_length=200)
    category = models.CharField(
        choices=CategoryType.get_list_of_tuples(), max_length=200
    )
    units = models.CharField(
        choices=UnitType.get_list_of_tuples(), max_length=200
    )
