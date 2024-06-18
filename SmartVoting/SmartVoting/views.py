from django.shortcuts import render
from users.forms import VoterRegistrationForm


def index(request):
    return render(request, 'index.html', {})
    # return render(request, 'GetUserPics.html', {})

def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})

def UserLogin(request):
    return render(request, 'UserLogin.html', {})


def UserRegister(request):
    form = VoterRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})