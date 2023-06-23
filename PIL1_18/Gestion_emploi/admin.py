from django.contrib import admin
from .models import création_emploie_du_temps

# Register your models here.
class Admincréation_emploie_du_temps(admin.ModelAdmin):
    list_display = ('Num_Emplois', 'Promotion_Emplois', 'Libellé_Mat','Horaire_Mat', 'Temps_restant_Mat', 'Nom_professeur', 'Prénom_Professeur', 'Date_cours', 'Début_cours', 'Fin_cours')
admin.site.register(création_emploie_du_temps, Admincréation_emploie_du_temps)