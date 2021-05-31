from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'username or password is incorrect')
            return redirect('login')
    return render(request, 'signup.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password2 == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, f'username  {username} is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, f'email id {email} is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, last_name=last_name, first_name=first_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'both password are incorrect ')
            return redirect('register')




    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')