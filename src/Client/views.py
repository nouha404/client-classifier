from django.shortcuts import render
from .forms import SignForm
from joblib import load
from pathlib import Path
import pandas as pd


# Create your views here.
def Formulaire(request):
    if request.method == 'POST':
        form = SignForm(request.POST)

        full_path = Path(__file__).parent / 'saveModel' / 'superModel.joblib'
        model = load(full_path)

        if form.is_valid():
            age = form.cleaned_data['age']
            marital = form.cleaned_data['etat_civile']
            job = form.cleaned_data['profession']
            education = form.cleaned_data['education']
            default = form.cleaned_data['defaut_de_paiement']
            loan = form.cleaned_data['pret_immobilier']
            housing = form.cleaned_data['pret_personnel']
            pdays = form.cleaned_data['dernier_contact_avec_le_client']
            previous = form.cleaned_data['contacts_precedent']

            # liste de noms de colonnes valides dans le model deja entrainné
            features = ['age', 'marital', 'job', 'education', 'default', 'loan', 'housing', 'pdays', 'previous']
            # Préparer les données pour la prédiction
            data = [{'age': int(age), 'marital': int(marital), 'job': int(job), 'education': int(education),
                     'default': int(default), 'loan': int(loan), 'housing': int(housing), 'pdays': int(pdays),
                     'previous': int(previous)}]
            # dataframe avec les données et les noms de colonnes
            df = pd.DataFrame(data, columns=features)

            eyes_pred = model.predict(df)
            answer = 'Vous etes un bon client GG 🔥' if eyes_pred[0] == 0 else "Vous n'etes pas fiable ⛔"
            return render(request, 'Client/resultat.html', {'answer': answer})
    else:
        form = SignForm()
    return render(request, 'Client/Formulaire.html', {'form': form})