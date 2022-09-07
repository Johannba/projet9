from django.shortcuts import render


def followers(request):
    return render(request, 'followers/followers.html')
