from django import forms
from .models import création_emploie_du_temps

class FormEmploi(forms.ModelForm):
    class Meta:
        model = création_emploie_du_temps
       
        fields = ['Num_Emplois', 'Promotion_Emplois', 'Libellé_Mat', 'Horaire_Mat', 'Temps_restant_Mat', 'Nom_professeur', 'Prénom_Professeur', 'Date_cours', 'Début_cours', 'Fin_cours', 'Bat_cours', 'Salle_cours', 'Date_exam', 'Début_exam', 'Fin_exam']




    