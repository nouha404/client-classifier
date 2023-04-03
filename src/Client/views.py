import os.path
from pathlib import Path

from django.shortcuts import render
from .forms import SignForm
from joblib import load
from pathlib import Path

from joblib import load
import numpy as np


# Create your views here.
def Formulaire(request):
    if request.method == 'POST':
        form = SignForm(request.POST)

        full_path = Path(__file__).parent / 'saveModel' / 'superModel.joblib'
        model = load(full_path)

        if form.is_valid():
            age = form.cleaned_data['age']
            marital = form.cleaned_data['marital']
            job = form.cleaned_data['job']
            education = form.cleaned_data['education']
            default = form.cleaned_data['default']
            housing = form.cleaned_data['housing']
            loan = form.cleaned_data['loan']
            pdays = form.cleaned_data['pdays']
            previous = form.cleaned_data['previous']

            # Préparer les données pour la prédiction
            df = [[int(age), int(marital), int(job), int(education), int(default), int(housing), int(loan), int(pdays),
                   int(previous)]]
            eyes_pred = model.predict(df)
            answer = ['Vous etes un bon client GG' if eyes_pred[0] == 0 else "Vous n'etes pas fiable"]

            return render(request, 'Client/resultat.html', {'answer': answer})
    else:
        form = SignForm()
    return render(request, 'Client/Formulaire.html', {'form': form})
