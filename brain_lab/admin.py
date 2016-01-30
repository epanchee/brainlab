from django.contrib import admin
from brain_lab.models import Visitor, RegResult, SurveyList, PartInSurveys, Visit, Sibling

for i in (Visitor, RegResult, SurveyList, PartInSurveys, Visit, Sibling):
    admin.site.register(i)
