from django.contrib import admin
from .models import Emplois

class AdminEmplois(admin.ModelAdmin):
    list_display = ('id_emploie','semaine','promotion','matière','masse_horaire', 'temps_restant','professeur','salle', 'jour', 'heure_debut', 'heure_fin')
admin.site.register(Emplois, AdminEmplois)


