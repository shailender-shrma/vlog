from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from post.views import Show_post

def Signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            data = User.objects.create_user(email=email,username=username,password=password1)
            data.save()
            return redirect('login')
        else:
            return redirect('signup')
    return render(request,'templates/register.html')


def Login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('showpost')
        else:
            return render (request,'templates/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'templates/login.html')
   

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request,"templates/index.html")
    else:
        return render(request, "templates/index.html")

# def Show_post(request):
    
#     return render(request, 'templates/index.html')