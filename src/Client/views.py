from django.shortcuts import render
from .forms import SignForm
from joblib import load
from pathlib import Path


# Create your views here.
def Formulaire(request):
    if request.method == 'POST':
        form = SignForm(request.POST)

        full_path = Path(__file__).parent / 'saveModel' / 'superModel.joblib'
        model = load(full_path)

        if form.is_valid():
            age = form.cleaned_data['age']
            etat_civile = form.cleaned_data['etat_civile']
            profession = form.cleaned_data['profession']
            education = form.cleaned_data['education']
            defaut_de_paiement = form.cleaned_data['defaut_de_paiement']
            pret_immobilier = form.cleaned_data['pret_immobilier']
            pret_personnel = form.cleaned_data['pret_personnel']
            dernier_contact = form.cleaned_data['dernier_contact_avec_le_client']
            contacts_precedent = form.cleaned_data['contacts_precedent']

            # Préparer les données pour la prédiction
            df = [[int(age), int(etat_civile), int(profession), int(education), int(defaut_de_paiement), int(pret_immobilier), int(pret_personnel), int(dernier_contact),
                   int(contacts_precedent)]]
            eyes_pred = model.predict(df)
            answer = 'Vous etes un bon client GG 🔥' if eyes_pred[0] == 0 else "Vous n'etes pas fiable ⛔"

            return render(request, 'Client/resultat.html', {'answer': answer})
    else:
        form = SignForm()
    return render(request, 'Client/Formulaire.html', {'form': form})
