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
            return redirect("flux")
    return render(request, 'flux/image_upload.html', context={'form': form})



def posts(request):
    return render(request, 'flux/posts.html')


def flux(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'flux/flux.html', context={'tickets': tickets})


