from django import forms

from brain_lab.models import Visitor, Sibling


class VisitorForm(forms.ModelForm):
    class Meta:
        models = Visitor
        fields = '__all__'

    Siblings = forms.ModelMultipleChoiceField(queryset=Sibling.objects.filter(visitor=2))
