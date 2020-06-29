from django.db import models
from essentials_kit_management.models import (
    Brand, Item, User
)


class UserItemStatus(models.Model):

    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivered_items = models.IntegerField()
    total_items_cost = models.IntegerField()
    cost_incurred = models.IntegerField()
