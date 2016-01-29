from django.contrib import admin
from brain_lab.models import Visitor, RegResult, SurveyList, PartInSurveys, Visit

for i in (Visitor, RegResult, SurveyList, PartInSurveys, Visit):
    admin.site.register(i)
