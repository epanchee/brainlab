# encoding=utf-8
from django.db import models
from multiselectfield import MultiSelectField


class Sibling(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО сиблинга')
    genger = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')), verbose_name='Пол сиблинга')
    birth = models.DateField(default=None, verbose_name='Дата рождения сиблинга')
    diag = models.TextField(blank=True, verbose_name='Диагноз сиблинга')
    inquirer = MultiSelectField(blank=True, verbose_name='Участие в опросниках',
                                choices=((1, 'WA Well-being – общее функционирование'), (2, 'SCQ'), (3, 'Коннерс')))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Сиблинг".encode('utf-8')
        verbose_name_plural = u"Сиблинги".encode('utf-8')


class Visitor(models.Model):
    VisitorID = models.AutoField(primary_key=True)  # Код ребенка
    FID1 = models.CharField(max_length=100, verbose_name='ФИО первого родителя')  # ФИО первого родителя
    FID2 = models.CharField(max_length=100, verbose_name='ФИО второго родителя', blank=True)  # ФИО второго родителя
    Mobile1 = models.CharField(max_length=13, verbose_name='Сотовый телефон 1')  # Сотовый телефон 1
    Mobile2 = models.CharField(max_length=13, blank=True, verbose_name='Сотовый телефон 2')  # Сотовый телефон 2
    Home_number = models.CharField(max_length=13, blank=True, verbose_name='Домашний телефон')  # Домашний телефон
    Addr = models.CharField(max_length=255, verbose_name='Адрес')  # Адрес
    Country = models.CharField(max_length=255, verbose_name='Страна', blank=True, null=True)
    Oblast = models.CharField(max_length=255, verbose_name='Область', blank=True, null=True)
    City = models.CharField(max_length=255, verbose_name='Город', blank=True, null=True)
    Street = models.CharField(max_length=255, verbose_name='Улица', blank=True, null=True)
    House = models.IntegerField(verbose_name='Номер дома', blank=True, null=True)
    Korpus = models.IntegerField(verbose_name='Корпуса', blank=True, null=True)
    Flat = models.IntegerField(verbose_name='Квартира', blank=True, null=True)
    Floor = models.FloatField(verbose_name='Этажность дома', blank=True, null=True)
    Side = MultiSelectField(blank=True, null=True, verbose_name='Сторона света',
                            choices=((1, 'С'), (2, 'СВ'), (3, 'В'), (4, 'ЮВ'),
                                     (5, 'Ю'), (6, 'ЮЗ'), (7, 'З'), (8, 'СЗ')))
    BuildingMaterial = models.CharField(max_length=255, verbose_name='Материал стен дома', blank=True, null=True)
    Email = models.EmailField(verbose_name='E-mail')
    ChildName = models.CharField(max_length=50, verbose_name='ФИО ребенка')  # ФИО ребенка
    BirthDate = models.DateField(verbose_name='Дата рождения ребенка')  # Дата рождения ребенка
    CorrectedBirthDate = models.DateField(verbose_name='Скорретированная дата рождения (заполняется автоматически)',
                                          blank=True, null=True, editable=False)
    LastVisit = models.DateField(verbose_name='Дата последнего посещения (заполняется автоматически)', blank=True,
                                 null=True)
    Comment = models.TextField(verbose_name='Комментарии', blank=True)
    ChildGenger = models.CharField(max_length=1, choices=((u'М', 'Мужской'), (u'Ж', 'Женский')),
                                   verbose_name='Пол ребенка')  # Пол ребенка
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

    Lang1 = models.CharField(max_length=50,
                             verbose_name='Первый язык, на котором говорят в семье')  # Первый язык, на котором говорят в семье
    Perc1 = models.IntegerField(verbose_name='% слышимости первого языка')  # % слышимости первого языка
    Lang2 = models.CharField(max_length=50, blank=True, null=True, default=None,
                             verbose_name='Второй язык, на котором говорят в семье')  # Первый язык, на котором говорят в семье
    Perc2 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name='% слышимости второго языка')  # % слышимости второго языка

    Q1 = models.CharField(max_length=100, blank=True,
                          verbose_name='Род занятий 1го родителя')  # Род занятий 1го родителя
    Q2 = MultiSelectField(blank=True, verbose_name='Квалификация 1го родителя', choices=(
        (1, "Среднее образование (оконченное)"),
        (2, "Среднее образование (неоконченное)"),
        (3, "Среднеспециальное образование (оконченное)"),
        (4, "Среднеспециальное образование (неоконченное)"),
        (5, "Высшее образование (оконченное)"),
        (6, "Высшее образование (неоконченное)"),
        (7, "Ученая степень")))  # Квалификация 1го родителя
    Q3 = models.CharField(max_length=100, blank=True,
                          verbose_name='Род занятий 2го родителя')  # Род занятий 2го родителя
    Q4 = MultiSelectField(blank=True, verbose_name='Квалификация 2го родителя', choices=(
        (1, "Среднее образование (оконченное)"),
        (2, "Среднее образование (неоконченное)"),
        (3, "Среднеспециальное образование (оконченное)"),
        (4, "Среднеспециальное образование (неоконченное)"),
        (5, "Высшее образование (оконченное)"),
        (6, "Высшее образование (неоконченное)"),
        (7, "Ученая степень")))  # Квалификация 2го родителя
    Q5 = models.BooleanField(blank=True, verbose_name='РАС в семье (да/нет)')  # Аустисты в семье (да/нет)
    Q6 = MultiSelectField(blank=True, verbose_name='Кто?', choices=(
        (1, 'Мать'), (2, 'Отец'), (3, 'Отец'), (4, 'Брат'), (5, 'Сестра'), (6, 'Бабушка'),
        (7, 'Дедушка')))  # Кто?
    Q7 = models.BooleanField(blank=True, verbose_name='СДВГ в семье (да/нет)')  # Сдвг в семье (да/нет)
    Q8 = MultiSelectField(blank=True, verbose_name='Кто?', choices=(
        (1, 'Мать'), (2, 'Отец'), (3, 'Отец'), (4, 'Брат'), (5, 'Сестра'), (6, 'Бабушка'),
        (7, 'Дедушка')))  # Кто?
    Q9 = models.BooleanField(blank=True,
                             verbose_name='Цветовая слепота в семье (да/нет)')  # Цветовая слепота в семье (да/нет)
    Q10 = MultiSelectField(blank=True, verbose_name='Кто?', choices=(
        (1, 'Мать'), (2, 'Отец'), (3, 'Отец'), (4, 'Брат'), (5, 'Сестра'), (6, 'Бабушка'),
        (7, 'Дедушка')))  # Кто?
    Surveys = MultiSelectField(blank=True, verbose_name='Участие в исследованиях', choices=(
        (1, 'Риск развити РАС '), (2, 'Риск развития СДВГ'), (3, 'Ишемический инсульт'), (4, 'Группа сравнения'),
        (5, 'Недоношенные, отслеживание по паспортному возрасту'),
        (6, 'Недоношенные, отслеживание по скорректированному возрасту'), (7, 'Дети с ГИПЦНС'), (8, 'Другие')))
    IsInvited = models.BooleanField(blank=True, default=False, verbose_name='Ребенок приглашен на исследования?')

    InnerID = models.CharField(max_length=20, blank=True, null=True, verbose_name='Шифр ребенка')

    app_label = 'brain_lab'
    model_name = 'visitor'

    def __unicode__(self):
        return self.ChildName

    def __str__(self):
        return self.ChildName

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
    ContExt = models.CharField(max_length=100, blank=True,
                               verbose_name='Дополнения к контактировию')  # Дополнения к контактировию
    Joined = models.BooleanField(
        verbose_name='Присоединился ли к исследованиям (да/нет)')  # Присоединился ли к исследованиям (да/нет)
    ReasNotJoined = models.CharField(max_length=100, blank=True,
                                     verbose_name='Причина, по которой не присоединился')  # Причина, по которой не присоединился
    NeurConsult = models.BooleanField(verbose_name='Консультация невролога (да/нет)')  # Консультация невролога (да/нет)

    def __unicode__(self):
        return self.ChildFIO

    class Meta:
        verbose_name = u"Регистрация".encode('utf-8')
        verbose_name_plural = u"Регистрация".encode('utf-8')


class Visit(models.Model):
    VisitID = models.AutoField(primary_key=True)  # ID визита
    VisitorID = models.ForeignKey(Visitor, verbose_name='Ребенок (посетитель)')  # Код ребенка
    VisitDate = models.DateField(default=None, verbose_name='Дата визита')  # Дата визита
    VisitAge = models.IntegerField(blank=True, default=0,
                                   verbose_name="Нормализованный возраст визита")  # нормализованный в виде месяц = 30 дней => год = 360 дней
    CorrectedVisitAge = models.FloatField(null=True, default=None, blank=True, editable=False,
                                          verbose_name='Скорректированный возраст визита в месяцах')
    InformAgreement = models.BooleanField(verbose_name='Информированное согласие')
    MedData = models.BooleanField(verbose_name='Медицинские сведения (карточка)')
    ET = MultiSelectField(blank=True, verbose_name='Eye tracking', choices=(
        (1, 'Popout scenes'), (2, 'Visual search'), (3, 'Gaze following'), (4, 'Pupil measure'),
        (5, 'Gap-overlap')))
    Photogrmetr = models.BooleanField(verbose_name='Фотограмметрия')
    Henotype = models.BooleanField(blank=True, verbose_name='Генотипирования')
    AntroData = MultiSelectField(blank=True, verbose_name='Антропометрические данные',
                                 choices=((1, 'Измерение головы'), (2, 'Вес, рост')))
    MRI = models.BooleanField(verbose_name='Сделали МРТ?')
    EEG = models.BooleanField(verbose_name='Сделали ЭЭГ?')  # Сделали ЭЭГ
    Neuro = models.BooleanField(verbose_name='Прошли осмотр у невролога?', default=False)
    PCI = models.BooleanField(verbose_name='PCI')
    ADOS = models.BooleanField(verbose_name='ADOS')
    Bailey = MultiSelectField(blank=True, verbose_name='Бэйли',
                              choices=((1, 'Основная часть'), (2, 'Опросник')))  # Сделали Бэйли
    Inquirer = MultiSelectField(blank=True, verbose_name='Участие в опросниках', choices=(
        (1, 'Речевое развитие'), (2, 'WA Well-being – общее функционирование'), (3, 'SCQ'),
        (4, 'Социальные данные'), (5, 'Медицинская история'),
        (6, 'Vineland'), (7, 'ADI-R'),
        (8, 'Target child updates – изменения в развитии'), (9, 'МакАртур – с комментариями'), (10, 'IBQ'),
        (11, 'Сенсорный профиль'), (12, 'Опросник сна 1'), (13, 'Опросник сна 2'),
        (14, 'Milestones – вехи развития'),
        (15, 'Parent-Infant caregiver(забота о ребенке)'), (16, 'M-Chart'), (17, 'SRS'),
        (18, 'Демографические данные'),
        (19, 'CBCL')))
    EndOfSurvey = models.BooleanField(verbose_name='Закончили ли обследование')  # Закончили ли обследование
    Feedback = models.BooleanField(verbose_name='Отдали обратную связь')  # Отдали обратную связь

    class Meta:
        verbose_name = u"Посещение".encode('utf-8')
        verbose_name_plural = u"Посещения".encode('utf-8')

    def __unicode__(self):
        return "%s %s" % (self.VisitorID.ChildName, self.VisitDate)

    def __str__(self):
        return "%s %s" % (self.VisitorID.ChildName, self.VisitDate)
