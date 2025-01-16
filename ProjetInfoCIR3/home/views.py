from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ProjetInfoCIR3.BDD.Fonction_db import Get_Utilisateur, Add_Match, Get_Match, Get_Equipe, Get_Utilisateur

@login_required
def home(request):
    user_name = request.user.username  # Get the current user's name
    user_list = Get_Utilisateur()
    current_user = next((user for user in user_list if user['pseudo'] == user_name), None)
    user_role = current_user['status'] if current_user else None
    return render(request, 'home.html', {'user_role': user_role})

@login_required
def manage_matches(request):
    if request.method == 'POST':
        equipe1 = request.POST['equipe1']
        equipe2 = request.POST['equipe2']
        date = request.POST['date']
        score1 = request.POST['score1']
        score2 = request.POST['score2']
        winner = request.POST['winner']
        referee = request.POST['referee']
        Add_Match(equipe1, equipe2, date, score1, score2, winner, referee)
        return redirect('manage_matches')
    
    matches = Get_Match()
    squads = Get_Equipe()
    referees = [user for user in Get_Utilisateur() if user['status'] == 'referee']
    return render(request, 'manager/manage_matches.html', {'matches': matches, 'squads': squads, 'referees': referees})

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page

def role_management(request):
    # Page that allows the user to manage other users' roles. Managers and admin can set the role of other users (except admin, which can only be set by another admin)
    return render(request, 'role_management.html')