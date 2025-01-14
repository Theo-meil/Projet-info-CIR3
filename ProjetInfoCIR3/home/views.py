from django.shortcuts import render
from django.contrib.auth.decorators import login_required   

@login_required
def home(request):
    return render(request, 'home.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"})
