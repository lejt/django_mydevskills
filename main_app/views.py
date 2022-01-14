from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def skills_index(request):
    return render(request, 'skills_index.html')

def signup(request):
    pass