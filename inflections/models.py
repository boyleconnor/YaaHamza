from django.db.models import Model, TextField, ForeignKey
from arabic_utils.constants import GENDER_CHOICES, STATE_CHOICES, COUNT_CHOICES, PERSON_CHOICES, TENSE_MOOD_CHOICES, \
    CASE_CHOICES


class Inflection(Model):
    spelling = TextField()
    stem = ForeignKey('dictionary.Word', related_name='inflections')

    def properties(self):
        return {'gender': self.gender, 'state': self.state, 'count': self.count, 'person': self.person,
                'tense/mood': self.tense_mood, 'case': self.case}

    def __str__(self):
        return self.spelling


class AdjectiveInflection(Inflection):
    case = TextField(choices=CASE_CHOICES)
    count = TextField(choices=COUNT_CHOICES)
    gender = TextField(choices=GENDER_CHOICES)
    state = TextField(choices=STATE_CHOICES)


class NounInflection(Inflection):
    case = TextField(choices=CASE_CHOICES)
    count = TextField(choices=COUNT_CHOICES)
    state = TextField(choices=STATE_CHOICES)


class Conjugation(Inflection):
    gender = TextField(choices=GENDER_CHOICES)
    person = TextField(choices=PERSON_CHOICES)
    tense_mood = TextField(choices=TENSE_MOOD_CHOICES)