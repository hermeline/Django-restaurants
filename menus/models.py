from django.db import models

# Create your models here.

class Menu(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(max_length=255)
    entree = models.CharField(max_length=255)
    plat = models.CharField(max_length=200)
    dessert = models.CharField(max_length=200)



    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.nom
