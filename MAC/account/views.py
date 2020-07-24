from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request,'account/signup.html')


def signup(request):
    if request.method =='POST':
        mail = request.POST.get('email','')
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        conf_pass = request.POST.get('confpass')


        userCheck= User.objects.filter(username=username) | User.objects.filter(email = mail)
        if userCheck:# checking username
            messages.error(request,'Username or email already Taken')
            return redirect('/account')



        if password == conf_pass:#cheking password
            user_obj = User.objects.create_user(first_name=name,password=password,email=mail,username=username)
            user_obj.save()
        return redirect('/account')


def userlogin(request):
    if request.method == "POST":
        user_name =request.POST.get('username','')
        user_pass =request.POST.get('password','')

        user = authenticate(username=user_name,password=user_pass)
        if user is not None:
            login(request,user)
            messages.success(request,'logged in successful')
            return redirect('/userpage')
        else:
            messages.error(request,'invalid credentials')
            return redirect('/account')

def userlogout(request):
    logout(request)
    messages.success(request,'successfully logged out')
    return redirect('/account')










