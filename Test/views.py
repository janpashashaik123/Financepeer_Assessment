from typing import AbstractSet
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('ReadJson.html')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('Login.html')

    else:
        return render(request,"Login.html")

def signup(request):
    if request.method=='POST':
        username=request.POST['uname']
        firstname=request.POST['fname']
        lastname=request.POST['lname'] 
        email=request.POST['email']
        password=request.POST['pass']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('Signup.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Already Exist')
            return redirect('Signup.html')
        else:
            a=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            a.save()
            print("User Created")
            return redirect('/')
    else:
        return render(request,"Signup.html")
def read(request):
    if request.method=='POST':
        uploaded_file= request.FILES['doc']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request,'ReadJson.html')