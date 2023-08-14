from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def Show_post(request):
    poost = Post.objects.all()   
    context={"ppost":poost}
    
    return render(request, 'templates/index.html', context)


@login_required
def Add_post(request):
    if request.method=='POST':

        form = PostForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.author=request.user
            obj.save()
            # form.instance.author = self.request.user
            return render(request, 'templates/index.html')
        else:
            form = PostForm()
    return render(request, "templates/post_add.html")
        
            # if title is None & content is None:




   
