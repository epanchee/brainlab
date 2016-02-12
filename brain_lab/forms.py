from dal import autocomplete
from django import forms

from brain_lab.models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        widgets = {
            'VisitorID': autocomplete.ModelSelect2(url='visitor-autocomplete')
        }

    def save(self, commit=True):
        self.instance.VisitAge = (self.instance.VisitDate - self.instance.VisitorID.BirthDate).days / 30
        return super(VisitForm, self).save(commit)
