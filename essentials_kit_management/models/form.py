from django.db import models


class Form(models.Model):

    form_name = models.CharField(max_length=200)
    closed_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField()
