from django.contrib import admin
from django.urls import path, include
from question import views as question_views

urlpatterns = [
    path('', question_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('panel_uzytkownika/', question_views.panel_uzytkownika, name='panel_uzytkownika'),
    path('login/', question_views.user_login, name='login'),  # Dodaj tę ścieżkę do logowania
    path('registration/', question_views.registration_view, name='registration'),
    path('dodaj_pytanie/', question_views.dodaj_pytanie, name='dodaj_pytanie'),
    path('edytuj_pytanie/<int:pytanie_id>/', question_views.edytuj_pytanie, name='edytuj_pytanie'),
    path('usun_pytanie/<int:pytanie_id>/', question_views.usun_pytanie, name='usun_pytanie'),
    path('question/', include('django.contrib.auth.urls')),  # Ta linia jest niezbędna do obsługi wbudowanych widoków logowania Django
]
