# coding=utf-8
import datetime
from django.contrib import admin


class ExplorationsFilter(admin.SimpleListFilter):
    title = 'Фильтр по исследованиям'

    parameter_name = 'Surveys'

    def lookups(self, request, model_admin):
        return (
            (1, 'Риск развити РАС '), (2, 'Риск развития СДВГ'), (3, 'Ишемический инсульт'), (4, 'Группа сравнения'),
            (5, 'Недоношенные, отслеживание по паспортному возрасту'),
            (6, 'Недоношенные, отслеживание по скорректированному возрасту'), (7, 'Дети с ГИПЦНС'), (8, 'Другие')
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
            age_in_days = datetime.datetime.now() - datetime.timedelta(int(self.value()) * 30)
            delta = datetime.timedelta(30)  # shifts by 5 days each year (30*12 = 360; 365-360 = 5)
            return queryset.filter(BirthDate__range=(age_in_days - delta, age_in_days))
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
            age_in_days = datetime.datetime.now() - datetime.timedelta(int(self.value()) * 30)
            delta = datetime.timedelta(30)  # shifts by 5 days each year (30*12 = 360; 365-360 = 5)
            return queryset.filter(CorrectedBirthDate__range=(age_in_days - delta, age_in_days))
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

class ETFilter(admin.SimpleListFilter):
    title = 'Фильтр по Eye Tracking'

    parameter_name = 'ET'

    def lookups(self, request, model_admin):
        return (
            (1, 'Popout scenes'), (2, 'Visual search'), (3, 'Gaze following'), (4, 'Pupil measure'),
            (5, 'Gap-overlap')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(ET__contains=self.value())
        return queryset

class BaileyFilter(admin.SimpleListFilter):
    title = 'Фильтр по Bailey'

    parameter_name = 'Bailey'

    def lookups(self, request, model_admin):
        return ((1, 'Основная часть'), (2, 'Опросник'))

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(Bailey__contains=self.value())
        return queryset

class InquirerFilter(admin.SimpleListFilter):
    title = 'Фильтр по опросникам'

    parameter_name = 'Inquirer'

    def lookups(self, request, model_admin):
        return (
            (1, 'Речевое развитие'), (2, 'WA Well-being – общее функционирование'), (3, 'SCQ'),
            (4, 'Социальные данные'), (5, 'Медицинская история'),
            (6, 'Vineland'), (7, 'ADI-R'),
            (8, 'Target child updates – изменения в развитии'), (9, 'МакАртур – с комментариями'), (10, 'IBQ'),
            (11, 'Сенсорный профиль'), (12, 'Опросник сна 1'), (13, 'Опросник сна 2'),
            (14, 'Milestones – вехи развития'),
            (15, 'Parent-Infant caregiver(забота о ребенке)'), (16, 'M-Chart'), (17, 'SRS'),
            (18, 'Демографические данные'),
            (19, 'CBCL')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(Inquirer__regex= "(^|,)%s(,|$)" % self.value())
        return queryset