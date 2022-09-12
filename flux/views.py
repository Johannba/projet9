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
            image = form.save(commit=False)
            image.uploader = request.user
            image.save()
            return redirect("home")
    return render(request, 'flux/image_upload.html', context={'form': form})

@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    print(tickets[0].title)
    return render(request, 'flux/home.html', context={'tickets': tickets})
# Create your views here.


def posts(request):
    return render(request, 'flux/posts.html')


def flux(request):
    return render(request, 'flux/flux.html')


