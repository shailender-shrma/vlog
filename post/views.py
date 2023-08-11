from django.shortcuts import render
from .models import Post
# Create your views here.
def show_post(request):
    s_post = Post.objects.all()
    context = {'s_post':s_post}
    print(s_post)

    return render(request, 'templates/index.html')
