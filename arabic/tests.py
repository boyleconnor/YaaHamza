from django.test import TestCase
from arabic.constants import ABJAD, SHADDA, FATHA
from arabic.models import *


class ArabicTests(TestCase):
    def setUp(self):
        for i, j in {'فعل': 'do; make', 'كتب': 'write', 'طبخ': 'cook; prepare food'}.items():
            Root.objects.create(spelling=i, definition=j)
        deriver = Deriver.objects.create(name='form I (fatHa)', match=('([%s])' % ABJAD) * 3,
                                         template=('\\1%s\\2%s\\3%s' % ((FATHA,) * 3)),
                                         pos='verb', properties='form:I')
        [deriver.apply(i) for i in Root.objects.filter(id__lte=3)]
        deriver2 = Deriver.objects.create(name='form II', match=('([%s])' % ABJAD) * 3,
                                          template=('\\1%s\\2%s%s\\3%s' % (FATHA, FATHA, SHADDA, FATHA)),
                                          pos='verb', properties='form:II')
        [deriver2.apply(i) for i in Root.objects.filter(id__lte=3)]

    def test_derivatives(self):
        self.assertEqual(6, len(Word.objects.all()))
        for i in Word.objects.all():
            print(i)
            print(i.definition)