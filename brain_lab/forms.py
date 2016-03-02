# coding=utf-8
import datetime

from dal import autocomplete
from django import forms

from brain_lab.models import Visit, Visitor

NORMAL_GESTATION = 37  # нормальный срок беременности (в неделях)


def get_norm_visit_age(birthdate, visitdate):
    days = (visitdate.year - birthdate.year) * 360 + (visitdate.month - birthdate.month) * 30 + (visitdate.day - birthdate.day)
    return days


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        widgets = {
            'VisitorID': autocomplete.ModelSelect2(url='visitor-autocomplete')
        }

    def save(self, commit=True):
        self.instance.CorrectedVisitAge = get_norm_visit_age(self.instance.VisitorID.CorrectedBirthDate, self.instance.VisitDate)
        self.instance.NormalizedVisitAge = get_norm_visit_age(self.instance.VisitorID.BirthDate, self.instance.VisitDate)

        if self.instance.VisitorID.LastVisit:
            if self.instance.VisitorID.LastVisit <= self.instance.VisitDate:
                self.instance.VisitorID.LastVisit = self.instance.VisitDate
        else:
            self.instance.VisitorID.LastVisit = self.instance.VisitDate
            print(self.instance.VisitorID.LastVisit)
        self.instance.VisitorID.save(commit)

        return super(VisitForm, self).save(commit)


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'

    def save(self, commit=True):
        if self.instance.Gestination < 37:
            self.instance.CorrectedBirthDate = self.instance.BirthDate + datetime.timedelta(
                (NORMAL_GESTATION - self.instance.Gestination) * 7)
        else:
            self.instance.CorrectedBirthDate = self.instance.BirthDate
        return super(VisitorForm, self).save(commit)
