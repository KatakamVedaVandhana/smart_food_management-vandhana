from django.db import models
from essentials_kit_management.models import (
    Form, Section, Brand
)

class Item(models.Model):

    item_name = models.CharField(max_length=200)
    description = models.TextField()
    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    section_name = models.ForeignKey('Section', on_delete=models.CASCADE)
    brand = models.ForeignKey("Item", on_delete=models.CASCADE)
