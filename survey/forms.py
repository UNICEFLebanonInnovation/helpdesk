import datetime
from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
CURRENT_YEAR = datetime.datetime.now().year


class ResearchForm(forms.ModelForm):
    # publication_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    publication_year = forms.ChoiceField(choices=list(((str(x), x) for x in range(CURRENT_YEAR - 5, CURRENT_YEAR + 5))),
                                         initial=CURRENT_YEAR)