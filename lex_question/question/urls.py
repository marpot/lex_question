from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.zadaj_pytanie, name='zadaj_pytanie'),
    path('panel_uzytkownika/', views.panel_uzytkownika, name='panel_uzytkownika'),  # Dodaj ścieżkę do panelu użytkownika
    path('registration/', views.registration_view, name='registration')
]
