from django.contrib import admin
from django.urls import path, include
from question import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('panel_uzytkownika/', views.panel_uzytkownika, name='panel_uzytkownika'),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('dodaj_pytanie/', views.dodaj_pytanie, name='dodaj_pytanie'),
    path('edytuj_pytanie/<int:pytanie_id>/', views.edytuj_pytanie, name='edytuj_pytanie'),
]
