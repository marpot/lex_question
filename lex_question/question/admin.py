from django.contrib import admin

from .models import Pytanie

@admin.register(Pytanie)
class PytanieAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'data_publikacji')
    search_fields = ['tytul', 'tresc']