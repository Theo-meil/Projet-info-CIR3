from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from ProjetInfoCIR3.BDD.Fonction_db import Add_utilisateur

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user in MongoDB
            Add_utilisateur(
                nom=request.POST['first_name'],
                prenom=request.POST['last_name'],
                pseudo=user.username,
                mot_de_pass=user.password,
                email=request.POST['email'],
                statut=request.POST['status'],  # get status from form
            )
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
