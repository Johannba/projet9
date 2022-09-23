from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    choice_value = [('1', '- 1'), ('2', '- 2'), ('3', '- 3'), ('4', '- 4'), ('5', '- 5')]
    rating = forms.ChoiceField(label='Note', widget=forms.RadioSelect, choices=choice_value)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body', ]



