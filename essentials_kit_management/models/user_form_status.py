from django.db import models
from essentials_kit_management.models import (
    Form, User
)


class UserFormStatus(models.Model):

    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    total_items_cost = models.IntegerField()
    total_items = models.IntegerField()
    pending_items = models.IntegerField()
    cost_incurred = models.IntegerField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)