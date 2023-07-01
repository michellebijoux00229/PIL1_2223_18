from django.shortcuts import render, get_object_or_404
from listing.models import Emplois, ModificationEmploi

def modify_emploi(request, emploi_id):
    emploi = get_object_or_404(Emplois, id_emploie=emploi_id)

    if request.method == 'POST':
        # Récupérer les données du formulaire de modification de l'emploi du temps
        semaine = request.POST.get('semaine')
        promotion = request.POST.get('promotion')
        matiere = request.POST.get('matiere')
        masse_horaire = request.POST.get('masse_horaire')
        temps_restant = request.POST.get('temps_restant')
        professeur = request.POST.get('professeur')
        salle = request.POST.get('salle')
        jour = request.POST.get('jour')
        heure_debut = request.POST.get('heure_debut')
        heure_fin = request.POST.get('heure_fin')

        # Mettre à jour les champs de l'emploi du temps
        emploi.semaine = semaine
        emploi.promotion = promotion
        emploi.matiere = matiere
        emploi.masse_horaire = masse_horaire
        emploi.temps_restant = temps_restant
        emploi.professeur = professeur
        emploi.salle = salle
        emploi.jour = jour
        emploi.heure_debut = heure_debut
        emploi.heure_fin = heure_fin

        # Enregistrer les modifications dans la base de données
        emploi.save()

        # Rediriger l'utilisateur vers une page de confirmation ou autre
        return redirect('confirmation_page')

    return render(request, 'modify_emploi.html', {'emploi': emploi})
