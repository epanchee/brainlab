from django.contrib import admin

from brain_lab.forms import VisitorForm
from brain_lab.models import Visitor, RegResult, PartInSurveys, Visit, Sibling


@admin.register(Visitor, RegResult, PartInSurveys, Visit, Sibling)
class FooAdmin(admin.ModelAdmin):
    pass
    # form = VisitorForm
