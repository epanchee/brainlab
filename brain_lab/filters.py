# coding=utf-8
import datetime
from django.contrib import admin


class ExplorationsFilter(admin.SimpleListFilter):
    title = 'Фильтр по исследованиям'

    parameter_name = 'Surveys'

    def lookups(self, request, model_admin):
        return (
            (1, 'Риск развити РАС '), (2, 'Риск развития СДВГ'), (3, 'Ишемический инсульт'), (4, 'Группа сравнения'),
            (5, 'Недоношенные'), (6, 'Дети с ГИПЦНС'), (7, 'Другие')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(Surveys__contains=self.value())
        return queryset


class BirthDayFilter(admin.SimpleListFilter):
    title = 'Фильтр по дате рождения'

    parameter_name = 'BirthDate'

    def lookups(self, request, model_admin):
        return (
            (i, str(i) + ' месяцев') for i in [3, 5, 10, 14, 24, 36]
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset \
                .filter(BirthDate__lte=datetime.datetime.now() - datetime.timedelta(int(self.value()) * 30) - datetime.timedelta(7)) \
                .filter(BirthDate__gte=datetime.datetime.now() - datetime.timedelta(int(self.value()) * 30) + datetime.timedelta(7))
        return queryset


class CorrectedBDayFilter(admin.SimpleListFilter):
    title = 'Фильтр по скорректированной дате рождения'

    parameter_name = 'CorrectedBirthDate'

    def lookups(self, request, model_admin):
        return (
            (i, str(i) + ' месяцев') for i in [3, 5, 10, 14, 24, 36]
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset \
                .filter(CorrectedBirthDate__gte=datetime.datetime.now() - datetime.timedelta(int(self.value()) * 30) - datetime.timedelta(7)) \
                .filter(CorrectedBirthDate__lte=datetime.datetime.now() - datetime.timedelta(int(self.value()) * 30) + datetime.timedelta(7))
        return queryset


class HasSiblingsFilter(admin.SimpleListFilter):
    title = 'Фильтр по наличию сиблингов'

    parameter_name = 'Siblings'

    def lookups(self, request, model_admin):
        return (
            (1, 'Есть'), (2, 'Нет')
        )

    def queryset(self, request, queryset):
        if self.value() == u'1':
            return queryset.exclude(Siblings__isnull=True)
        if self.value() == u'2':
            return queryset.exclude(Siblings__isnull=False)
        return queryset
