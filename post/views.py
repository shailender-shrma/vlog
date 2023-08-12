from django.shortcuts import render
# from .models import Post
from django.http import HttpResponse
# Create your views here.
def show_post(request):
    return render(request, 'templates/index.html')

def login(request):
    return render(request, 'templates/login.html')
def register(request):
    return render(request,'templates/register.html')
    
