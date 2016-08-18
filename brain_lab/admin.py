# coding=utf-8
from datetime import datetime

from django.contrib import admin

from brain_lab.filters import ExplorationsFilter, BirthDayFilter, CorrectedBDayFilter, HasSiblingsFilter, ETFilter, BaileyFilter, InquirerFilter
from brain_lab.forms import VisitForm, VisitorForm, get_norm_visit_age
from brain_lab.models import Visitor, RegResult, Visit, Sibling


def tostring_age(age):
    str_age = '-'
    if age:
        str_age = "%d месяцев, %d дней" % (age / 30, age % 30)
    return str_age


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    filter_horizontal = ("Siblings",)
    readonly_fields = ("passport_age", "corrected_age",)
    list_filter = (
        BirthDayFilter, CorrectedBDayFilter, ExplorationsFilter, HasSiblingsFilter, 'ChildGenger', 'IsInvited',
    )
    list_display = ('ChildName', 'ChildGenger', 'BirthDate', 'CorrectedBirthDate', 'IsInvited',)
    search_fields = ('^InnerID',)

    form = VisitorForm

    def passport_age(self, instance):
        age = get_norm_visit_age(instance.BirthDate, datetime.now())
        return tostring_age(age)
    passport_age.short_description = 'Возраст по паспорту'

    def corrected_age(self, instance):
        age = get_norm_visit_age(instance.BirthDate, datetime.now(), instance.Gestination)
        return tostring_age(age)
    corrected_age.short_description = 'Скорректированный возраст'


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    readonly_fields = ('visit_age', 'corrected_age',)
    fields = (
        'VisitorID', 'VisitDate', 'visit_age', 'corrected_age', 'InformAgreement', 'MedData', 'ET', 'Photogrmetr',
        'Henotype',
        'AntroData',
        'MRI', 'EEG', 'Neuro', 'PCI', 'ADOS', 'Bailey', 'Inquirer', 'EndOfSurvey', 'Feedback')
    list_display = ('VisitorID', 'VisitDate', 'EndOfSurvey', 'Feedback',)
    list_filter = ('EndOfSurvey', 'Feedback', 'EEG', 'PCI', ETFilter, BaileyFilter, InquirerFilter)

    def visit_age(self, instance):
        return tostring_age(instance.VisitAge)
    visit_age.short_description = 'Возраст во время визита'

    def corrected_age(self, instance):
        return tostring_age(instance.CorrectedVisitAge)
    corrected_age.short_description = 'Скорректированный возраст во время визита'

    form = VisitForm


@admin.register(RegResult, Sibling)
class FooAdmin(admin.ModelAdmin):
    pass
