from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("senha diferente!!")
        else:

            my_user=User.objects.create_user(email,'',pass1)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        psw=request.POST.get('password')
        user=authenticate(request,username=username,password=psw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username ou Password estão errado!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')