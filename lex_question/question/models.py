from django.db import models

class Pytanie(models.Model):
    tytul = models.CharField(max_length=100)
    tresc = models.TextField()
    data_publikacji = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul
