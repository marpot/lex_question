from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import FormularzPytania
from .forms import LoginForm
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def zadaj_pytanie(request):
    if request.method == 'POST':
        formularz = FormularzPytania(request.POST)
        if formularz.is_valid():
            formularz.save()
            return redirect('strona_glowna')  # Przekierowanie do strony głównej po zadaniu pytania
    else:
        formularz = FormularzPytania()
    return render(request, 'zadaj_pytanie.html', {'formularz': formularz})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Przekieruj użytkownika na panel użytkownika
                return redirect('panel_uzytkownika')
            else:
                # Dodaj komunikat błędu w przypadku nieudanego logowania
                error_message = "Nieprawidłowy login lub hasło. Spróbuj ponownie."
                return render(request, 'index.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})


def panel_uzytkownika(request):
    return render(request, 'panel_uzytkownika.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('panel_uzytkownika')  # Przekierowanie po udanej rejestracji
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})