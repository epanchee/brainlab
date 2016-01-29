# encoding=utf-8
from django.db import models


class Sibling(models.Model):
    VisitorID = models.ForeignKey('Visitor')
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя сиблинга')
    genger = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), blank=True, verbose_name='Пол сиблинга')
    birth = models.DateField(blank=True, null=True, default=None, verbose_name='Дата рождения сиблинга')
    diag = models.TextField(blank=True, verbose_name='Диагноз сиблинга')


class Visitor(models.Model):
    VisitorID = models.AutoField(primary_key=True)  # Код ребенка
    FID1 = models.CharField(max_length=100, verbose_name='ФИО первого родителя')  # ФИО первого родителя
    FID2 = models.CharField(max_length=100, verbose_name='ФИО второго родителя', blank=True)  # ФИО второго родителя
    Mobile1 = models.CharField(max_length=13, verbose_name='Сотовый телефон 1')  # Сотовый телефон 1
    Mobile2 = models.CharField(max_length=13, blank=True, verbose_name='Сотовый телефон 2')  # Сотовый телефон 2
    Home_number = models.CharField(max_length=13, blank=True, verbose_name='Домашний телефон')  # Домашний телефон
    Addr = models.CharField(max_length=255, verbose_name='Адрес')  # Адрес
    Email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    ChildName = models.CharField(max_length=50, verbose_name='ФИО ребенка')  # ФИО ребенка
    BirthDate = models.DateField(verbose_name='Дата рождения ребенка')  # Дата рождения ребенка
    ChildGenger = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), verbose_name='Пол ребенка')  # Пол ребенка
    Gestination = models.IntegerField(blank=True, default=0, verbose_name='Срок беременности в неделях')  # Срок беременности в неделях
    Birthweight = models.FloatField(blank=True, default=0.0, verbose_name='Вес при рождении')  # Вес при рождении
    ComplatBirth = models.IntegerField(verbose_name='Серьезные осложнения при рождении', blank=True, default=0)
    CBAnnot = models.TextField(verbose_name='Описание осложнений', blank=True)
    ProblAfBirth = models.IntegerField(verbose_name='Врожденные пороки или генетические заболевания', blank=True, default=0)
    PBAnnot = models.TextField(verbose_name='Описание заболеваний', blank=True)

    S1name = models.CharField(max_length=100, blank=True, verbose_name='Имя первого сиблинга')  # Имя первого сиблинга
    S1sex = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), blank=True, verbose_name='Пол первого сиблинга')  # Пол первого сиблинга
    S1birth = models.DateField(blank=True, null=True, default=None, verbose_name='Дата рождения первого сиблинга')  # Дата рождения первого сиблинга
    S1diag = models.TextField(blank=True, verbose_name='Диагноз первого сиблинга')  # Диагноз первого сиблинга
    S2name = models.CharField(max_length=50, blank=True, verbose_name='Имя второго сиблинга')
    S2sex = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), blank=True, verbose_name='Пол первого сиблинга')
    S2birth = models.DateField(blank=True, null=True, default=None, verbose_name='Дата рождения второго сиблинга')
    S2diag = models.CharField(max_length=100, blank=True, verbose_name='Диагноз второго сиблинга')
    S3name = models.CharField(max_length=50, blank=True, verbose_name='Имя третьего сиблинга')
    S3sex = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), blank=True)
    S3birth = models.DateField(blank=True, null=True, default=None)
    S3diag = models.CharField(max_length=100, blank=True)
    S4name = models.CharField(max_length=50, blank=True)
    S4sex = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), blank=True)
    S4birth = models.DateField(blank=True, null=True, default=None)
    S4diag = models.CharField(max_length=100, blank=True)
    Lang1 = models.IntegerField(blank=True, null=True, default=None)  # Первый язык, на котором говорят в семье
    Perc1 = models.IntegerField(blank=True, null=True, default=None)  # % слышимости первого языка
    Lang2 = models.IntegerField(blank=True, null=True, default=None)  # Первый язык, на котором говорят в семье
    Perc2 = models.IntegerField(blank=True, null=True, default=None)  # % слышимости второго языка

    Q1 = models.CharField(max_length=100, blank=True)  # Род занятий 1го родителя
    Q2 = models.CharField(max_length=100, blank=True)  # Квалификация 1го родителя
    Q3 = models.CharField(max_length=100, blank=True)  # Род занятий 2го родителя
    Q4 = models.CharField(max_length=100, blank=True)  # Квалификация 2го родителя
    Q5 = models.BooleanField()  # Аустисты в семье (да/нет)
    Q6 = models.CharField(max_length=100, blank=True)  # Кто?
    Q7 = models.BooleanField()  # Сдвг в семье (да/нет)
    Q8 = models.CharField(max_length=100, blank=True)  # Кто?
    Q9 = models.BooleanField()  # Цветовая слепота в семье (да/нет)
    Q10 = models.CharField(max_length=100, blank=True)  # Кто?

    def __str__(self):
        return self.ChildName.encode('utf-8')


class RegResult(models.Model):
    VisitorID = models.ForeignKey(Visitor)  # Код ребенка
    Directed = models.CharField(max_length=100, blank=True)  # Кем направлен
    Contacted = models.BooleanField()  # Контактировали (да/нет)
    ContExt = models.CharField(max_length=100, blank=True)  # Дополнения к контактировию
    Joined = models.BooleanField()  # Присоединился ли к исследованиям (да/нет)
    ReasNotJoined = models.CharField(max_length=100, blank=True)  # Причина, по которой не присоединился
    NeurConsult = models.BooleanField()  # Консультация невролога (да/нет)
    ChID = models.IntegerField(blank=True, null=True, default=None)  # Шифр ребенка (для основной базы)

    def __str__(self):
        return self.VisitorID.ChildName.encode('utf-8')


class SurveyList(models.Model):
    SurID = models.AutoField(primary_key=True)  # код исследования
    SurName = models.CharField(max_length=100)  # название исследования

    def __str__(self):
        return self.SurName.encode('utf-8')


class PartInSurveys(models.Model):
    PID = models.AutoField(primary_key=True)
    VisitorID = models.ForeignKey(Visitor)  # Код ребенка
    SurID = models.ForeignKey(SurveyList)  # Код исследования

    def __str__(self):
        return "%s %s" % (self.VisitorID.ChildName.encode('utf-8'), self.SurID)


class Visit(models.Model):
    VisitID = models.AutoField(primary_key=True)  # ID визита
    VisitorID = models.ForeignKey(Visitor)  # Код ребенка
    VisitDate = models.DateField(default=None)  # Дата визита
    VisitAge = models.IntegerField(default=None)  # Возраст визита (в месяцах)
    ET = models.BooleanField()  # Сделали EyeTracker
    EEG = models.BooleanField()  # Сделали ЭЭГ
    Bailey = models.BooleanField()  # Сделали Бэйли
    Inquirer = models.BooleanField()  # Сделали опросники
    EndOfSurvey = models.BooleanField()  # Закончили ли обследование
    Feedback = models.BooleanField()  # Отдали обратную связь

    def __str__(self):
        return "%s %s" % (self.VisitorID.ChildName.encode('utf-8'), self.VisitDate)
