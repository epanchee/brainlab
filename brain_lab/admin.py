# coding=utf-8
from django.contrib import admin

from brain_lab.filters import ExplorationsFilter, BirthDayFilter, CorrectedBDayFilter
from brain_lab.forms import VisitForm, VisitorForm
from brain_lab.models import Visitor, RegResult, Visit, Sibling


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    filter_horizontal = ("Siblings",)
    list_filter = (BirthDayFilter, CorrectedBDayFilter, ExplorationsFilter,)
    list_display = ('ChildName', 'ChildGenger', 'BirthDate', 'CorrectedBirthDate',)

    form = VisitorForm


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    readonly_fields = ('visit_age',)
    fields = (
        'VisitorID', 'VisitDate', 'visit_age', 'InformAgreement', 'MedData', 'ET', 'Photogrmetr', 'Henotype',
        'AntroData',
        'MRI', 'EEG', 'PCI', 'ADOS', 'Bailey', 'Inquirer', 'EndOfSurvey', 'Feedback')
    list_display = ('VisitorID', 'VisitDate',)

    def visit_age(self, instance):
        visitage = '-'
        if instance.VisitAge:
            visitage = "%d месяцев, %d дней" % (instance.VisitAge / 30, instance.VisitAge % 30)
        return visitage

    visit_age.short_description = 'Возраст во время визита'

    form = VisitForm


@admin.register(RegResult, Sibling)
class FooAdmin(admin.ModelAdmin):
    pass
