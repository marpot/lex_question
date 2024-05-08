from django.db import models
from django.contrib.auth.models import User

class Pytanie(models.Model):
    tytul = models.CharField(max_length=100)
    tresc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Ustawienie null=True
    data_publikacji = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul
    
class Odpowiedz(models.Model):
    pytanie = models.ForeignKey(Pytanie, related_name='odpowiedzi', on_delete=models.CASCADE)
    tresc = models.CharField(max_length=5000)
    data_odpowiedzi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Odpowiedź na pytanie: {self.pytanie.tytul}"