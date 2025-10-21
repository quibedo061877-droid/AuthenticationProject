from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *



def Home(request):
    return render(request, 'index.html')

def RegisterView(request):
    return render(request, 'register.html')

def LoginView(request):
    return render(request, 'login.html')