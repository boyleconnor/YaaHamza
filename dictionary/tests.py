from django.test import TestCase
from arabic_tools.utils import spelling_to_template
from dictionary.models import Word, Deriver


class ArabicTests(TestCase):
    def setUp(self):
        Word.objects.create(spelling='فعل', definition='doing; making', pos='root')
        Word.objects.create(spelling='طَاَلِب', definition='student', pos='noun')
        Deriver.objects.create(origin_pos='root', result_pos='verb', template=spelling_to_template('فَعَلَ'))

    def test_roots(self):
        for i in Word.objects.filter(pos='root'):
            print(i)
            print(i.definition)

    def test_nouns(self):
        for i in Word.objects.filter(pos='noun'):
            print(i)
            print(i.definition)

    def test_derivation(self):
        fa3ala = Deriver.objects.get(id=1).apply(Word.objects.get(id=1, pos='root', spelling='فعل'))
        print(fa3ala)
        self.assertEqual(fa3ala.spelling, 'فَعَلَ')