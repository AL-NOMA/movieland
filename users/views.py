from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print("here !!!")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                print("user created")
                return redirect("login")
        else:
            print("password not matching ...")
        
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     raw_password = form.cleaned_data.get('password1')
        #     user = authenticate(username=username, password=raw_password)
        #     login(request, user)
        #     return redirect('/')
    return render(request, 'users/register.html')


def login_view(request):
    return render(request, 'users/login.html')
