from django.db import models


class Brand(models.Model):

    brand_name = models.CharField(max_length=300)
    max_quantity = models.IntegerField()
    price = models.IntegerField()
