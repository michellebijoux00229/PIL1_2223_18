from django.shortcuts import render
from .models import création_emploie_du_temps
from .form import FormEmploi 
from django.db import IntegrityError
from django.contrib import messages

def Edition_emploi(request, *args, **kwargs):
    return render(request, 'Edition.html')

def Rempli_emploi(request,*args, **kwargs):
      instances = création_emploie_du_temps.objects.all
      return render(request, 'editer.html', {'instances': instances})
    
      

def Rempli_emploi(request):
    if request.method == 'POST':
        form = FormEmploi(request.POST)
        if form.is_valid():
            
            try:
                form.save()
                messages.success(request, "Les données ont été enregistrées avec succès.")
            except IntegrityError:
                messages.error(request, "Une erreur d'intégrité s'est produite lors de l'enregistrement des données.")
    else:
        form = FormEmploi()
    
    return render(request, 'editer.html', {'form': form})


                




