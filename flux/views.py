from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from . import forms
from . import models


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("flux")
    return render(request, 'flux/image_upload.html', context={'form': form})


@login_required
def create_review(request):
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("review_form")
    return render(request, 'flux/create_review.html', context={'form': form})



def posts(request):
    return render(request, 'flux/posts.html')


def flux(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'flux/flux.html', context={'tickets': tickets})


def review_flux(request):
    reviews = models.Review.objects.all()
    return render(request, 'flux/review_form.html', context={'reviews': reviews})


def response_ticket(request, ticket_id):
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = models.Ticket.objects.get(pk=ticket_id)
            review.save()
            return redirect("review_form")
    return render(request, 'flux/create_review.html', context={'form': form})