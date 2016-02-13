# coding=utf-8
import datetime
from django.contrib import admin


class ExplorationsFilter(admin.SimpleListFilter):
    title = 'Фильтр по исследованиям'

    parameter_name = 'ET'

    def lookups(self, request, model_admin):
        return (
            (1, 'Popout'), (2, 'Visual search'), (3, 'Gaze following'), (4, 'Scenes'), (5, 'Pupil measure'),
            (6, 'Gap-overlap')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(ET__contains=self.value())
        return queryset


class BirthDayFilter(admin.SimpleListFilter):
    title = 'Фильтр по дате рождения'

    parameter_name = 'BirthDate'

    def lookups(self, request, model_admin):
        return (
            (i, str(i) + ' месяцев') for i in range(6, 61, 6)
        )

    def queryset(self, request, queryset):
        if self.value():
            queryset = queryset.filter(
                BirthDate__lte=datetime.datetime.now() - datetime.timedelta(int(self.value()) * 30))
            return queryset.filter(
                BirthDate__gt=datetime.datetime.now() - datetime.timedelta((int(self.value()) + 6) * 30))
        return queryset
