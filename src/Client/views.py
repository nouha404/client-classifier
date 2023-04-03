from django.shortcuts import render
from .forms import SignForm


# Create your views here.
def Formulaire(request):
    if request.method == 'POST':
        form = SignForm(request.POST)

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
            return render(request, 'Client/resultat.html')
    else:
        form = SignForm()
    return render(request, 'Client/Formulaire.html', {'form': form})
