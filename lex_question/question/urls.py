from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dodaj_pytanie/', views.dodaj_pytanie, name='dodaj_pytanie'),
    path('edytuj_pytanie/<int:pytanie_id>/', views.edytuj_pytanie, name='edytuj_pytanie'),
    path('usun_pytanie/<int:pytanie_id>/', views.usun_pytanie, name='usun_pytanie'),
    path('login/', views.user_login, name='login'),
    path('panel_uzytkownika/', views.panel_uzytkownika, name='panel_uzytkownika'),
    path('registration/', views.registration_view, name='registration'),
]