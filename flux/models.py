from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=5000)
    image = models.ImageField()

