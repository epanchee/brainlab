# coding=utf-8
import datetime
import random

from django.test import TestCase

from brain_lab.models import *


class VisitorTestCase(TestCase):
    def setUp(self):
        Sibling.objects.create(name='test sibling', genger=u'М', birth=datetime.date.fromordinal(
            random.randint(datetime.date.min.toordinal(), datetime.date.max.toordinal())))
        Visitor.objects.create(FID1='test', Mobile1='+7456123456', Addr='address', Email='email@exmaple.com',
                               ChildName='Child name', BirthDate=datetime.date.today(), ChildGenger=u'Ж', Gestination=1,
                               Q5=False, Q7=False, Q9=False, Q11=False,
                               Birthweight=3, Lang1=1, Perc1=1)

    def test_visitor(self):
        visitor = Visitor.objects.get(FID1='test')
        self.assertEqual(visitor.FID1, 'test')
        self.assertEqual(visitor.ChildName, 'Child name')
