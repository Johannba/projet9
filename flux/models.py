from django.conf import settings
from django.db import models
from django import forms


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=5000)
    image = models.ImageField()

