from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model

def Register(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1!=password2:
            return render('templates/register.html')
        else:
            return render('templates/index.html')
        
        user = User.objects.create_user(username,email,firstname,lastname)

        user.firstname = firstname
        user.lastname = lastname
        user.save()

        return render(request,'templates/login.html')
    return render(request, 'templates/register.html')
