from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Pytanie
from .forms import FormularzPytania

def index(request):
    return render(request, 'index.html')

def dodaj_pytanie(request):
    if request.method == 'POST':
        formularz = FormularzPytania(request.POST)
        if formularz.is_valid():
            pytanie = formularz.save(commit=False)
            pytanie.uzytkownik = request.user
            pytanie.save()
            return redirect('panel_uzytkownika')
    else:
        formularz = FormularzPytania()
    return render(request, 'panel_uzytkownika.html', {'formularz': formularz})

def usun_pytanie(request, pytanie_id):
    pytanie = get_object_or_404(Pytanie, id=pytanie_id)
    if request.method == 'POST':
        pytanie.delete()
        return redirect('index')
    return render(request, 'usun_pytanie.html', {'pytanie': pytanie})

def edytuj_pytanie(request, pytanie_id):
    pytanie = get_object_or_404(Pytanie, id=pytanie_id)
    if request.method == 'POST':
        formularz = FormularzPytania(request.POST, instance=pytanie)
        if formularz.is_valid():
            formularz.save()
            return redirect('index')
    else:
        formularz = FormularzPytania(instance=pytanie)
    return render(request, 'edytuj_pytanie.html', {'formularz': formularz})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Zalogowano pomyślnie.")
                print("Użytkownik zalogowany:", username)
                return redirect('panel_uzytkownika')  # Przekierowanie do panelu użytkownika po zalogowaniu
            else:
                messages.error(request, "Nieprawidłowy login lub hasło. Spróbuj ponownie.")
                print("Nieprawidłowy login lub hasło.")
        else:
            messages.error(request, "Formularz logowania jest nieprawidłowy.")
            print("Formularz logowania jest nieprawidłowy.")
    else:
        form = LoginForm()
    print("Widok user_login został wywołany.")
    return redirect('panel_uzytkownika')  # Przekierowanie do panelu użytkownika po zalogowaniu



@login_required
def panel_uzytkownika(request):
    return render(request, 'panel_uzytkownika.html')  # Renderowanie szablonu panelu użytkownika

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
                return redirect('login')  # Przekierowanie po udanej rejestracji na stronę logowania
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
