import datetime
from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
CURRENT_YEAR = datetime.datetime.now().year

YES_NO_CHOICE = (
    (True, 'Yes'),
    (False, 'No')
)


class ResearchForm(forms.ModelForm):
    # publication_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    publication_year = forms.ChoiceField(choices=list(((str(x), x) for x in range(CURRENT_YEAR - 5, CURRENT_YEAR + 5))),
                                         initial=CURRENT_YEAR)


class InfoTrackerForm(forms.ModelForm):
    validated_by_technical_committee = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO_CHOICE, initial=False)
    validated_by_moph = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO_CHOICE, initial=False)
