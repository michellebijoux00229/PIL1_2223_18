from django.db import models
from django.core.mail import send_mail
from django.conf import settings

class Emplois(models.Model):
    id_emploi = models.SmallAutoField(primary_key=True)
    semaine = models.CharField(max_length=255)
    promotion = models.CharField(max_length=255, null=False, blank=False)
    matiere = models.CharField(max_length=255)
    masse_horaire = models.PositiveIntegerField()
    temps_restant = models.PositiveIntegerField()
    professeur = models.CharField(max_length=255)
    salle = models.CharField(max_length=30)
    jour = models.CharField(max_length=30)
    heure_debut = models.TimeField(auto_now=False, auto_now_add=False)
    heure_fin = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Emplois"
        verbose_name_plural = "Emplois"

class ModificationEmploi(models.Model):
    emploi = models.ForeignKey(Emplois, on_delete=models.CASCADE)
    date_modification = models.DateTimeField(auto_now_add=True)
    modifie_par = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        # Enregistrer la modification dans la base de données
        super().save(*args, **kwargs)

        # Envoyer un e-mail aux étudiants concernés
        etudiants = self.emploi.promotion.etudiant_set.all()
        sujet = 'Modification de l\'emploi du temps'
        message = f"L'emploi du temps a été modifié : {self.description}"
        destinataires = [etudiant.email for etudiant in etudiants]
        send_mail(sujet, message, settings.DEFAULT_FROM_EMAIL, destinataires, fail_silently=True)

    class Meta:
        verbose_name = "Modification de l'emploi du temps"
        verbose_name_plural = "Modifications de l'emploi du temps"
