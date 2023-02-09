from django.db import models


class Categories(models.Model):
    nom_categorie = models.CharField(max_length=45)

    def __str__(self):
        return self.nom_categorie
