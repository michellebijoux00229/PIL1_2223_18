from django.db import models

class Emplois(models.Model):
    id_emploie = models.SmallAutoField(primary_key=True)  
    semaine = models.CharField(max_length=255)
    promotion = models.CharField(max_length=255, null=False, blank=False)
    matière = models.CharField(max_length=255)
    masse_horaire = models.PositiveIntegerField()
    temps_restant = models.PositiveIntegerField()
    professeur = models.CharField(max_length=255)
    salle =  models.CharField(max_length=30)
    jour = models.CharField(max_length=30)
    heure_debut = models.TimeField(auto_now=False, auto_now_add=False)
    heure_fin = models.TimeField(auto_now=False, auto_now_add=False)
   
    class Meta: 
        verbose_name = ("Emplois")
        verbose_name_plural = ("Emplois") 
