from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from . import forms
from . import models


@login_required
def image_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect("home")
    return render(request, 'flux/image_upload.html', context={'form': form})


@login_required
def home(request):
    image = models.Image.objects.all()
    return render(request, 'flux/home.html', context={'image': image})
# Create your views here.


def posts(request):
    return render(request, 'flux/posts.html')


def flux(request):
    return render(request, 'flux/flux.html')


