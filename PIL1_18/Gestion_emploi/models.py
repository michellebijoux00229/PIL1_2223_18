from django.db import models


class création_emploie_du_temps(models.Model):
        Num_Emplois = models.AutoField(primary_key=True)
        Promotion_Emplois = models.CharField(max_length=255, null=False, blank=False)
        Libellé_Mat = models.CharField(max_length=255)
        Horaire_Mat = models.IntegerField(editable=True)
        Temps_restant_Mat = models.IntegerField(editable=True)
        Nom_professeur = models.CharField(max_length=255)
        Prénom_Professeur = models.CharField(max_length=255)
        Date_cours = models.DateField()
        Début_cours = models.TimeField()
        Fin_cours = models.TimeField()
        Bat_cours = models.CharField(max_length=255)
        Salle_cours = models.CharField(max_length=255)
        Date_exam = models.DateField()
        Début_exam = models.TimeField()
        Fin_exam = models.TimeField()

        class Meta:
                verbose_name = ('création-emploie_du_temps')
                verbose_name_plural = ('création-emploie_du_temps')
        def __str__(self):
                return f" {self.Num_Emplois} - {self.Libellé_Mat} - {self.Horaire_Mat} - {self.Temps_restant_Mat}- {self.Nom_professeur}- {self.Prénom_Professeur}- {self.Date_cours}- {self.Début_cours} - {self.Fin_cours} - {self.Bat_cours} - {self.Salle_cours} - {self.Date_exam} - {self.Début_exam} - {self.Fin_exam}" 

