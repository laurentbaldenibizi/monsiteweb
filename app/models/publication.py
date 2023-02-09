from django.db import models
from app.models import Categories

class Publication(models.Model):
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de publication")                           


    def __str__(self):
        return self.titre
