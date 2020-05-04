from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .forms import AccountProfile

# Create your views here.
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)

    profile = AccountProfile()


    return render(request, 'profile.html', {"profile": profile})
