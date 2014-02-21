from django.contrib import auth
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'index.html', {})


def profile(request):
    return render(request, 'profile.html', {})
