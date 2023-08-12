from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.
def show_post(request):
    poost = Post.objects.all()    
    return render(request, 'templates/index.html' , {'poost':poost})

   
