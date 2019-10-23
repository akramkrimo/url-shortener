from django.db import models
import string
import random
# Create your models here.

class UrlShortcut(models.Model):
    raw_url = models.URLField()
    short_url = models.URLField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.short_url