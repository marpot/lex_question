from django import forms
from .models import Pytanie

class FormularzPytania(forms.ModelForm):
    class Meta:
        model = Pytanie
        fields = ['tytul', 'tresc']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Login')
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')