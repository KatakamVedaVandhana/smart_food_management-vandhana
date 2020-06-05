from django.db import models


class Announcements(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
    image = models.URLField()
