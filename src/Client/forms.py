from django import forms

MARITAL = ((1, 'marié(e)'), (2, 'célibataire'), (3, 'inconnu(e) '))
JOB = ((1, 'ouvrier'), (2, 'technicien'), (3, 'management'), (4, 'services'), (5, 'retraité(e)'),
       (6, 'administration'), (7, 'chômeur'), (8, 'entrepreneur'), (9, 'travailleur indépendant'), (10, 'femme/homme de ménage'),
       (11, 'étudiant(e)'))
STUDY = (
    (1, "niveau d'éducation basique (4 ans)"), (2, 'diplôme universitaire'), (3, 'inconnu(e)'), (4, 'professional course'), (5, "niveau d'éducation basique (9 ans)"),
    (6, "niveau d'éducation basique (6 ans)"))
DEFAULT = ((1, 'inconnu(e)'), (2, 'non'), (3, 'oui'))
HOUSING = ((1, 'inconnu(e)'), (2, 'non'), (3, 'oui'))
LOAN = ((1, 'non'), (2, 'oui'), (3, 'inconnu(e)'))


class SignForm(forms.Form):
    age = forms.IntegerField(min_value=10, required=True)
    etat_civile = forms.ChoiceField(choices=MARITAL, required=True)
    profession = forms.ChoiceField(choices=JOB, required=True)
    education = forms.ChoiceField(choices=STUDY, required=True)
    defaut_de_paiement = forms.ChoiceField(choices=DEFAULT, required=True)
    pret_immobilier = forms.ChoiceField(choices=HOUSING, required=True)
    pret_personnel = forms.ChoiceField(choices=LOAN, required=True)
    dernier_contact_avec_le_client = forms.IntegerField(min_value=0, max_value=999, required=True)
    contacts_precedent = forms.IntegerField(min_value=0, max_value=2, required=True)