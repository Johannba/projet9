from django.shortcuts import render
from django.shortcuts import redirect


def followers(request):
    if request.POST:
        username = request.POST['username']
        return redirect("followers")
    return render(request, 'followers/followers.html')
