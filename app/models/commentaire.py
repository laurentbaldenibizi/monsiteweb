from django.db import models
from app.models import Categories,Publication

class Commentaire(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    contenu=models.TextField(max_length=160)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de publication")
