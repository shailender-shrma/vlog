from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required


selected_user = ""


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
            
            return render(request, 'templates/index.html')
        else:
            form = PostForm()
    return render(request, "templates/post_add.html")


@login_required
# def edit_post(request, id):
#     if request.method=="POST":
#         update_post = get_object_or_404(Post,id=id,author=request.user)
#         form = PostForm(request.POST or None, obj=update_post)

#         if form.is_valid():
#             form.save()
#             return render(request,"templates/index.html")

#         return render(request, "templates/update.html")

def edit(request):
    user = request.user
    
    if user.is_authenticated:

        if request.method == "POST":
            id = request.POST.get('postid')
            content = request.POST.get('content')
            delete1 = request.POST.get('delete')
            if id != None:
                
                
                global selected_user
                selected_user = Post.objects.get(id=id)
                content = selected_user.content
                
                
                # selected_user.content = content
                # selected_user.save()


                return render(request, "templates/update_post.html", {'content':content})
            elif content!=None:
                
                selected_user.content = content
                selected_user.save()

                return render(request, "templates/index.html")
            elif delete1!=None:
                
                delete1=int(delete1)
                selected_user2 = Post.objects.get(pk=delete1)
                
                selected_user2.delete()

                return redirect('showpost')

    else:
        return render(request, "templates/login.html")
    



def User_blog_post(request):
    User_post=PostForm.objects.filter(author=request.user)
    user_post = {'user_post':User_post}
    return render(request, "showpost",user_post)

# # def del_post(request):
# def del_post(request):
#     user = request.user
    






   
