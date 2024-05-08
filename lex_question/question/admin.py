from django.contrib import admin
from .models import Pytanie, Odpowiedz

@admin.register(Pytanie)
class PytanieAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'data_publikacji')
    search_fields = ['tytul', 'tresc']
    
@admin.register(Odpowiedz)
class OdpowiedzAdmin(admin.ModelAdmin):
    list_display = ('tresc', 'data_odpowiedzi')  # Wyświetl tylko tresc i data_odpowiedzi
    search_fields = ['tresc']
