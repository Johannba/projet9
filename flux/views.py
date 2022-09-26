from django.contrib.auth.decorators import login_required
from django.db.models import Value, CharField
from django.shortcuts import redirect, render
from itertools import chain
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
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)

    tickets = tickets.annotate(contente_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(contente_type=Value('REVIEW', CharField()))

    posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)
    return render(request, 'flux/posts.html', context={'posts': posts})


def flux(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)

    tickets = tickets.annotate(contente_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(contente_type=Value('REVIEW', CharField()))

    posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)
    return render(request, 'flux/flux.html', context={'posts': posts})


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


def ticket_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST, request.FILES)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket = ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket.id
            review.save()
            return redirect("flux")
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'flux/ticket_review.html', context=context)
