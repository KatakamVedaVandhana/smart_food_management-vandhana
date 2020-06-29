from django.db import models
#from food_management.models.user import User
from food_management.models.meal import Meal

class UserFeedback(models.Model):
    user_id = models.IntegerField()
    #user = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
