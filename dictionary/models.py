from dictionary.utils.constants import GENDER_CHOICES, STATE_CHOICES, COUNT_CHOICES, PERSON_CHOICES, \
    TENSE_MOOD_CHOICES, CASE_CHOICES
from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, TextField, ForeignKey, OneToOneField, BooleanField


class Root(Model):
    spelling = TextField()
    definition = TextField()

    def __str__(self):
        return ' '.join([i for i in self.spelling])


class Word(Model):
    spelling = TextField()
    definition = TextField()
    examples = TextField()
    root = ForeignKey('Root', blank=True, null=True, related_name='derivatives')
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    gender = TextField(choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.spelling


class Adjective(Word):
    pass


class Noun(Word):
    gender = TextField(choices=GENDER_CHOICES)
    human = BooleanField()


class Verb(Word):
    verbal_noun = OneToOneField('Noun', blank=True, null=True, related_name='verb')
    active_participle = OneToOneField('Adjective', blank=True, null=True, related_name='verb')
    passive_participle = OneToOneField('Adjective', blank=True, null=True, related_name='verb')


class Preposition(Word):
    pass