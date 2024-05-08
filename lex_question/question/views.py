from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm, FormularzOdpowiedzi, FormularzPytania
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pytanie, Odpowiedz
from question import views as question_views


def index(request):
    return render(request, 'index.html')

@login_required
def dodaj_pytanie(request):
    if request.method == 'POST':
        formularz_pytania = FormularzPytania(request.POST)
        formularz_odpowiedzi = FormularzOdpowiedzi(request.POST)
        if formularz_pytania.is_valid():
            pytanie = formularz_pytania.save(commit=False)
            pytanie.author = request.user
            pytanie.save()
            if formularz_odpowiedzi.is_valid():
                odpowiedz = formularz_odpowiedzi.save(commit=False)
                odpowiedz.pytanie = pytanie
                odpowiedz.save()
                return redirect('panel_uzytkownika')
            else:
                messages.error(request, "Wypełnij pole treść odpowiedzi.")
        else:
            messages.error(request, "Formularz jest nieprawidłowy.")
    else:
        formularz_pytania = FormularzPytania()
        formularz_odpowiedzi = FormularzOdpowiedzi()
    return render(request, 'panel_uzytkownika.html', {'formularz_pytania': formularz_pytania, 'formularz_odpowiedzi': formularz_odpowiedzi})


def usun_pytanie(request, pytanie_id):
    pytanie = get_object_or_404(Pytanie, id=pytanie_id)
    if request.method == 'POST':
        pytanie.delete()
        return redirect('panel_uzytkownika')
    return render(request, 'usun_pytanie.html', {'pytanie': pytanie})

def edytuj_pytanie(request, pytanie_id):
    pytanie = get_object_or_404(Pytanie, id=pytanie_id)
    if request.method == 'POST':
        formularz = FormularzPytania(request.POST, instance=pytanie)
        if formularz.is_valid():
            formularz.save()
            messages.success(request, "Pomyślnie zaktualizowano pytanie.")
            return redirect('panel_uzytkownika')  # Przekierowanie do panelu użytkownika po zapisaniu zmian w pytaniu
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
    return render(request, 'login.html', {'form': form})


@login_required
def panel_uzytkownika(request):
    pytania_uzytkownika = Pytanie.objects.filter(author=request.user)
    odpowiedzi_uzytkownika = Odpowiedz.objects.filter(pytanie__author=request.user)
    return render(request, 'panel_uzytkownika.html', {'pytania_uzytkownika': pytania_uzytkownika})

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