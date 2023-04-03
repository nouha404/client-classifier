from django import forms

MARITAL = ((1, 'married'), (2, 'single'), (3, 'unknown'))
JOB = ((1, 'blue-collar : ouvrier'), (2, 'technician : technicien'), (3, 'management'), (4, 'services'), (5, 'retired'),
       (6, 'admin'), (7, 'unemployed : chômeur'), (8, 'entrepreneur'), (9, 'self-employed'), (10, 'housemaid'),
       (11, 'student'))
STUDY = (
    (1, 'basic.4y'), (2, 'university degree'), (3, 'unknown'), (4, 'professional course'), (5, 'basic.9y'),
    (6, 'basic.6y'))
DEFAULT = ((1, 'unknown'), (2, 'no'), (3, 'yes'))
HOUSING = ((1, 'unknown'), (2, 'no'), (3, 'yes'))
LOAN = ((1, 'no'), (2, 'yes'), (3, 'unknown'))


class SignForm(forms.Form):
    age = forms.IntegerField(min_value=10, required=True)
    marital = forms.ChoiceField(choices=MARITAL, required=True)
    job = forms.ChoiceField(choices=JOB, required=True)
    education = forms.ChoiceField(choices=STUDY, required=True)
    default = forms.ChoiceField(choices=DEFAULT, required=True)
    housing = forms.ChoiceField(choices=HOUSING, required=True)
    loan = forms.ChoiceField(choices=LOAN, required=True)
    pdays = forms.IntegerField(min_value=0, max_value=999, required=True)
    previous = forms.IntegerField(min_value=0, max_value=2, required=True)
