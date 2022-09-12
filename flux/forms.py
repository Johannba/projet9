from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']






