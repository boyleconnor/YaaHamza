from dictionary.utils.constants import GENDER_CHOICES, STATE_CHOICES, COUNT_CHOICES, PERSON_CHOICES, \
    TENSE_MOOD_CHOICES, CASE_CHOICES
from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, TextField, ForeignKey, OneToOneField, BooleanField


class Root(Model):
    spelling = TextField()
    definition = TextField()

    def __str__(self):
        return self.spelling


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
    active_participle = OneToOneField('Noun', blank=True, null=True, related_name='verb')
    passive_participle = OneToOneField('Noun', blank=True, null=True, related_name='verb')


class Preposition(Word):
    pass


class Inflection(Model):
    spelling = TextField()
    stem = ForeignKey('Word', related_name='inflections')
    #properties
    gender = TextField(choices=GENDER_CHOICES, blank=True)
    state = TextField(choices=STATE_CHOICES, blank=True)
    count = TextField(choices=COUNT_CHOICES, blank=True)
    person = TextField(choices=PERSON_CHOICES, blank=True)
    tense_mood = TextField(choices=TENSE_MOOD_CHOICES, blank=True)
    case = TextField(choices=CASE_CHOICES, blank=True)

    def properties(self):
        return {'gender': self.gender, 'state': self.state, 'count': self.count, 'person': self.person,
                'tense/mood': self.tense_mood, 'case': self.case}

    def __str__(self):
        return self.spelling