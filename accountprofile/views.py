from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User


# Create your views here.
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    username = User.objects.get(username=request.user.username)

    return render(request, 'profile.html')
