# encoding=utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from multiselectfield import MultiSelectField


class Sibling(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО сиблинга')
    genger = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), verbose_name='Пол сиблинга')
    birth = models.DateField(default=None, verbose_name='Дата рождения сиблинга')
    diag = models.TextField(blank=True, verbose_name='Диагноз сиблинга')

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u"Сиблинг".encode('utf-8')
        verbose_name_plural = u"Сиблинги".encode('utf-8')


# @python_2_unicode_compatible
class Visitor(models.Model):
    VisitorID = models.AutoField(primary_key=True)  # Код ребенка
    FID1 = models.CharField(max_length=100, verbose_name='ФИО первого родителя')  # ФИО первого родителя
    FID2 = models.CharField(max_length=100, verbose_name='ФИО второго родителя', blank=True)  # ФИО второго родителя
    Mobile1 = models.CharField(max_length=13, verbose_name='Сотовый телефон 1')  # Сотовый телефон 1
    Mobile2 = models.CharField(max_length=13, blank=True, verbose_name='Сотовый телефон 2')  # Сотовый телефон 2
    Home_number = models.CharField(max_length=13, blank=True, verbose_name='Домашний телефон')  # Домашний телефон
    Addr = models.CharField(max_length=255, verbose_name='Адрес')  # Адрес
    Email = models.EmailField(verbose_name='E-mail')
    ChildName = models.CharField(max_length=50, verbose_name='ФИО ребенка')  # ФИО ребенка
    BirthDate = models.DateField(verbose_name='Дата рождения ребенка')  # Дата рождения ребенка
    ChildGenger = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), verbose_name='Пол ребенка')  # Пол ребенка
    Gestination = models.IntegerField(verbose_name='Срок беременности в неделях')  # Срок беременности в неделях
    Birthweight = models.FloatField(verbose_name='Вес при рождении')  # Вес при рождении
    ComplatBirth = MultiSelectField(blank=True, verbose_name='Серьезные осложнения в перинатальном периоде',
                                    choices=(
                                        (1, 'Асфиксия'), (2, 'Гипоксически-ишемическое поражение ЦНС тяжелой степени'),
                                        (3, 'Кровоизлияния в головной мозг')))
    CBAnnot = models.TextField(verbose_name='Описание осложнений', blank=True)
    ProblAfBirth = MultiSelectField(verbose_name='Врожденные заболевания', blank=True, choices=(
        (1, 'Врожденные пороки развития ЦНС и внутренних органов'),
        (2, 'Заболевания, обусловленные хромосомными мутациями'),
        (3, 'Заболевания, обусловленные генетическими мутациями'),
        (4, 'Наследственные заболевания обена веществ')))
    PBAnnot = models.TextField(verbose_name='Описание заболеваний', blank=True)
    Diagnosis = models.TextField(verbose_name='Диагноз', blank=True)

    Siblings = models.ManyToManyField(Sibling, blank=True, verbose_name='Сиблинги')

    Lang1 = models.IntegerField(verbose_name='Первый язык, на котором говорят в семье')  # Первый язык, на котором говорят в семье
    Perc1 = models.IntegerField(verbose_name='% слышимости первого языка')  # % слышимости первого языка
    Lang2 = models.IntegerField(blank=True, null=True, default=None, verbose_name='Второй язык, на котором говорят в семье')  # Первый язык, на котором говорят в семье
    Perc2 = models.IntegerField(blank=True, null=True, default=None, verbose_name='% слышимости второго языка')  # % слышимости второго языка

    Q1 = models.CharField(max_length=100, blank=True, verbose_name='Род занятий 1го родителя')  # Род занятий 1го родителя
    Q2 = MultiSelectField(blank=True, verbose_name='Квалификация 1го родителя', choices=(
        (1, "Среднее образование (оконченное)"),
        (2, "Среднее образование (неоконченное)"),
        (3, "Среднеспециальное образование (оконченное)"),
        (4, "Среднеспециальное образование (неоконченное)"),
        (5, "Высшее образование (оконченное)"),
        (6, "Высшее образование (неоконченное)"),
        (7, "Ученая степень")))  # Квалификация 1го родителя
    Q3 = models.CharField(max_length=100, blank=True, verbose_name='Род занятий 2го родителя')  # Род занятий 2го родителя
    Q4 = MultiSelectField(blank=True, verbose_name='Квалификация 1го родителя', choices=(
        (1, "Среднее образование (оконченное)"),
        (2, "Среднее образование (неоконченное)"),
        (3, "Среднеспециальное образование (оконченное)"),
        (4, "Среднеспециальное образование (неоконченное)"),
        (5, "Высшее образование (оконченное)"),
        (6, "Высшее образование (неоконченное)"),
        (7, "Ученая степень")))  # Квалификация 2го родителя
    Q5 = models.BooleanField(blank=True, verbose_name='Аустисты в семье (да/нет)')  # Аустисты в семье (да/нет)
    Q6 = MultiSelectField(blank=True, verbose_name='Кто?', choices=(
        (1, 'Мать'), (2, 'Отец'), (3, 'Отец'), (4, 'Брат'), (5, 'Сестра'), (6, 'Бабушка'),
        (7, 'Дедушка')))  # Кто?
    Q7 = models.BooleanField(blank=True, verbose_name='Сдвг в семье (да/нет)')  # Сдвг в семье (да/нет)
    Q8 = MultiSelectField(blank=True, verbose_name='Кто?', choices=(
        (1, 'Мать'), (2, 'Отец'), (3, 'Отец'), (4, 'Брат'), (5, 'Сестра'), (6, 'Бабушка'),
        (7, 'Дедушка')))  # Кто?
    Q9 = models.BooleanField(blank=True, verbose_name='Цветовая слепота в семье (да/нет)')  # Цветовая слепота в семье (да/нет)
    Q10 = MultiSelectField(blank=True, verbose_name='Кто?', choices=(
        (1, 'Мать'), (2, 'Отец'), (3, 'Отец'), (4, 'Брат'), (5, 'Сестра'), (6, 'Бабушка'),
        (7, 'Дедушка')))  # Кто?
    Q11 = models.BooleanField(blank=True, verbose_name='Участие в опросах')

    InnerID = models.IntegerField(blank=True, null=True, verbose_name='Шифр ребенка')

    def __str__(self):
        return self.ChildName.encode('utf-8')

    class Meta:
        verbose_name = u"Ребенок".encode('utf-8')
        verbose_name_plural = u"Дети".encode('utf-8')


class RegResult(models.Model):
    ChildFIO = models.CharField(max_length=100, verbose_name='ФИО ребенка', default=None)
    BirthDate = models.DateField(verbose_name='Дата рождения ребенка', default=None)
    FIO = models.CharField(max_length=100, verbose_name='ФИО родителя', blank=True, default=None)
    Mob = models.CharField(max_length=13, verbose_name='Телефон для связи', blank=True, default=None)
    Email = models.EmailField(blank=True, verbose_name='E-mail')
    Directed = models.CharField(max_length=100, blank=True, verbose_name='Кем направлен')  # Кем направлен
    Contacted = models.BooleanField(verbose_name='Контактировали (да/нет)')  # Контактировали (да/нет)
    ContExt = models.CharField(max_length=100, blank=True, verbose_name='Дополнения к контактировию')  # Дополнения к контактировию
    Joined = models.BooleanField(verbose_name='Присоединился ли к исследованиям (да/нет)')  # Присоединился ли к исследованиям (да/нет)
    ReasNotJoined = models.CharField(max_length=100, blank=True, verbose_name='Причина, по которой не присоединился')  # Причина, по которой не присоединился
    NeurConsult = models.BooleanField(verbose_name='Консультация невролога (да/нет)')  # Консультация невролога (да/нет)

    def __str__(self):
        return self.VisitorID.ChildName.encode('utf-8')

    class Meta:
        verbose_name = u"Регистрация".encode('utf-8')
        verbose_name_plural = u"Регистрация".encode('utf-8')


# class SurveyList(models.Model):
#     SurID = models.AutoField(primary_key=True, verbose_name='Код исследования')  # код исследования
#     SurName = models.CharField(max_length=100, verbose_name='Название исследования')  # название исследования
#
#     def __str__(self):
#         return self.SurName.encode('utf-8')
#
#     class Meta:
#         verbose_name = u"Исследование".encode('utf-8')
#         verbose_name_plural = u"Список исследований".encode('utf-8')


class PartInSurveys(models.Model): # TODO: может перенести это в основную анкету?
    PID = models.AutoField(primary_key=True)
    VisitorID = models.ForeignKey(Visitor, verbose_name='Ребенок (посетитель)')  # Код ребенка TODO: to enable search among visitors (todo for all models)
    Surveys = MultiSelectField(blank=True, verbose_name='Исследования?', choices=(
        (1, 'Риск развити РАС '), (2, 'Риск развития СДВГ'), (3, 'Ишемический инсульт'), (4, 'Группа сравнения'),
        (5, 'Недоношенные'), (6, 'Дети с ГИПЦНС')))
    # SurID = models.ForeignKey(SurveyList, verbose_name='Исследование')  # Код исследования

    def __str__(self):
        return "%s" % (self.VisitorID.ChildName.encode('utf-8'))

    class Meta:
        verbose_name = u"Участие в опросах".encode('utf-8')
        verbose_name_plural = u"Участие в опросах".encode('utf-8')


class Visit(models.Model):
    VisitID = models.AutoField(primary_key=True)  # ID визита
    VisitorID = models.ForeignKey(Visitor, verbose_name='Ребенок (посетитель)')  # Код ребенка
    VisitDate = models.DateField(default=None, verbose_name='Дата визита')  # Дата визита
    VisitAge = models.IntegerField(default=0, verbose_name='Возраст визита (в месяцах)', editable=False)  # Возраст визита (в месяцах) TODO: to calculate age automatically
    ET = models.BooleanField(verbose_name='Сделали EyeTracker')  # Сделали EyeTracker
    EEG = models.BooleanField(verbose_name='Сделали ЭЭГ')  # Сделали ЭЭГ
    Bailey = models.BooleanField(verbose_name='Сделали Бэйли')  # Сделали Бэйли
    Inquirer = models.BooleanField(verbose_name='Сделали опросники')  # Сделали опросники
    EndOfSurvey = models.BooleanField(verbose_name='Закончили ли обследование')  # Закончили ли обследование
    Feedback = models.BooleanField(verbose_name='Отдали обратную связь')  # Отдали обратную связь

    def __str__(self):
        return "%s %s" % (self.VisitorID.ChildName.encode('utf-8'), self.VisitDate)

    class Meta:
        verbose_name = u"Посещение".encode('utf-8')
        verbose_name_plural = u"Посещения".encode('utf-8')
