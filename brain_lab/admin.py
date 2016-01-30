from django.contrib import admin

from brain_lab.models import Visitor, RegResult, SurveyList, PartInSurveys, Visit, Sibling


@admin.register(Visitor, RegResult, SurveyList, PartInSurveys, Visit, Sibling)
class FooAdmin(admin.ModelAdmin):
    pass
