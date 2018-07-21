from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('prodhome')
        else:
            return render(request, 'accounts/login.html', {'error': 'Please enter a valid a username and password.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # route to homepage
    # dont forget to logout
    if request.method=='POST':
        auth.logout(request)
        return redirect('prodhome')

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'user already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('prodhome')
        # for post
        else:
            #for get
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        #for get
        return render(request, 'accounts/signup.html')
