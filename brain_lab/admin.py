from django.contrib import admin

from brain_lab.forms import VisitForm
from brain_lab.models import Visitor, RegResult, Visit, Sibling


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    filter_horizontal = ("Siblings",)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass
    form = VisitForm


@admin.register(RegResult, Sibling)
class FooAdmin(admin.ModelAdmin):
    pass
