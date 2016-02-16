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
                               ChildName='Child name', BirthDate=datetime.date.today(), ChildGenger=u'Ж',
                               Gestination=35,
                               Q5=False, Q7=False, Q9=False, Birthweight=3, Lang1='Русский', Perc1=100,
                               IsInvited=False)

    def test_visitor(self):
        visitor = Visitor.objects.get(FID1='test')
        self.assertEqual(visitor.FID1, 'test')
        self.assertEqual(visitor.ChildName, 'Child name')
        self.assertEqual(visitor.Mobile1, '+7456123456')
        self.assertEqual(visitor.Addr, 'address')
        self.assertEqual(visitor.Email, 'email@exmaple.com')
        self.assertEqual(visitor.BirthDate, datetime.date.today())
        self.assertEqual(visitor.ChildGenger, u'Ж')
        self.assertEqual(visitor.Gestination, 35)
        self.assertEqual(visitor.IsInvited, False)
