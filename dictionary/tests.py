from django.test import TestCase
from dictionary.models import *


class ArabicTests(TestCase):
    def setUp(self):
        Root.objects.create(spelling='فعل', definition='do; make')
        Root.objects.create(spelling='كتب', definition='write')

    def test_roots(self):
        for i in Root.objects.all():
            print(i)
            print(i.properties)
            print(type(i.properties))
            print(i.definition)