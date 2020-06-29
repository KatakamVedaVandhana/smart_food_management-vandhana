from django.db import models


class Section(models.Model):

    section_name = models.CharField(max_length=300)