from brain_lab.models import Visit
from dal import autocomplete
from django import forms


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        widgets = {
            'VisitorID': autocomplete.ModelSelect2(url='visitor-autocomplete')
        }
