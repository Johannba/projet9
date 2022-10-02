from django import forms
from . import models


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class TicketFormDelete(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    choice_value = [('1', '- 1'), ('2', '- 2'), ('3', '- 3'), ('4', '- 4'), ('5', '- 5')]
    rating = forms.ChoiceField(label='Note', widget=forms.RadioSelect, choices=choice_value)
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body', ]


class ReviewFormDelete(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

