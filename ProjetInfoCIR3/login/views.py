from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
        #    auth_login(request, user)
        return redirect('home')
        #else:
        #    messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')
