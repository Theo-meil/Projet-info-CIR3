from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ProjetInfoCIR3.BDD.Fonction_db import Get_Utilisateur, Add_Match, Get_Match, Get_Equipe, Get_Utilisateur, Set_Match, Get_Event, Add_Event, Set_Event

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
        event = request.POST['event']
        if 'edit_match' in request.POST:
            match_id = request.POST['match_id']
            Set_Match(match_id, equipe1, equipe2, date, score1, score2, winner, referee, event)
        else:
            Add_Match(equipe1, equipe2, date, score1, score2, winner, referee, event)
        return redirect('manage_matches')
    
    matches = Get_Match()
    squads = Get_Equipe()
    referees = [user for user in Get_Utilisateur() if user['status'] == 'referee']
    events = Get_Event()
    print(events)
    return render(request, 'manager/manage_matches.html', {'matches': matches, 'squads': squads, 'referees': referees, 'events': events})

@login_required
def manage_events(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        date_debut = request.POST['date_debut']
        date_fin = request.POST['date_fin']
        places_max = request.POST['places_max']
        cash_price = request.POST['cash_price']
        status = request.POST['status']
        print("QUOICOUBEH")
        if 'edit_event' in request.POST:
            event_id = request.POST['event_id']
            #### TEMP SOLUTION #########
            # REPLACE WITH A QUERY TO THE "EVENT_SUBSCRIPTION" TABLE ONCE IMPLEMENTED
            places_libres = 5
            ############################
            Set_Event(event_id, nom, date_debut, date_fin, places_max, places_libres, cash_price, status)
        else:
            places_libres = places_max
            Add_Event(nom, date_debut, date_fin, places_max, places_libres, cash_price, status)
        return redirect('manage_events')
    
    events = Get_Event()
    return render(request, 'manager/manage_events.html', {'events': events})

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page

def role_management(request):
    # Page that allows the user to manage other users' roles. Managers and admin can set the role of other users (except admin, which can only be set by another admin)
    return render(request, 'role_management.html')