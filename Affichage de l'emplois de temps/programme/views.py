from django.shortcuts import render
from .models import Emplois

 
def consult(request1, *args, **kwargs):
    programme = Emplois.objects.all() 
    ordre_jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']
    jours_uniques = sorted(Emplois.objects.values_list('jour',flat=True).distinct(),key=lambda x: ordre_jours.index(x))
    context1 = {
        'programme':programme,
        'jours_uniques':jours_uniques,
    }    
    return render(request1, 'programme/consult.html', context1)




    #'jour':Emplois_du_temps.Jour_Emplois,
    #    'n':Emplois_du_temps.Num_groupe,
	 #   'Salle':Emplois_du_temps.Salle,
	  #  'debut':Emplois_du_temps.Heure_début_Emplois,
	   # 'fin':Emplois_du_temps.Heure_fin_Emplois,
       #	    'Matière':Emplois_du_temps.Matière_Emplois,
	    #'Temps':Emplois_du_temps.Temps_restant_Matière_Emplois,
	    #'Enseignant':Emplois_du_temps.Nom_professeur_Emplois


