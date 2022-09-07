from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'flux/home.html')
# Create your views here.


def posts(request):
    return render(request, 'flux/posts.html')


def flux(request):
    return render(request, 'flux/flux.html')


