from dictionary.utils.constants import POS_CHOICES, GENDER_CHOICES, STATE_CHOICES, COUNT_CHOICES, PERSON_CHOICES, \
    TENSE_MOOD_CHOICES, CASE_CHOICES
from django.core.urlresolvers import reverse
from django.db.models import Model, TextField, ForeignKey, ManyToManyField


class Root(Model):
    """
    Model for word root

    Ex: فعل, كتب, بسمل
    """
    spelling = TextField()
    definition = TextField()

    def __str__(self):
        return self.spelling


class Word(Model):
    """
    Model for fully-derived word

    Ex: مَطْبَخ, طَاَبِخ
    """
    spelling = TextField()
    definition = TextField()
    #relationships
    root = ForeignKey('Root', blank=True, null=True, related_name='derivatives')
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    #properties
    pos = TextField(choices=POS_CHOICES)
    gender = TextField(choices=GENDER_CHOICES, blank=True)

    def get_absolute_url(self):
        return reverse('word-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.spelling


class Inflection(Model):
    """
    Model for fully-inflected word

    Ex: كِتَاَبُ, كُتُبْ
    """
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