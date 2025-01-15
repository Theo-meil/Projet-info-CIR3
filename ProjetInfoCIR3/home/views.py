from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ProjetInfoCIR3.BDD.Fonction_db import Get_Utilisateur_Status

@login_required
def home(request):
    user_id = request.user.id
    user_role = Get_Utilisateur_Status(user_id)
    return render(request, 'home.html', {'user_role': user_role})


from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page

def role_management(request):
    # Page that allows the user to manage other users' roles. Managers and admin can set the role of other users (except admin, which can only be set by another admin)
    return render(request, 'role_management.html')