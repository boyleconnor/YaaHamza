from django.db.models import Model, TextField, ForeignKey


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