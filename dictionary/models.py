from django.core.urlresolvers import reverse_lazy

from django.db.models import Model, ForeignKey, CharField, TextField, NullBooleanField

from arabic_utils.constants import GENDER_CHOICES, POS_CHOICES, HUMAN_CHOICES


class Root(Model):
    spelling = TextField()
    definition = TextField()

    def __str__(self):
        return ' '.join([i for i in self.spelling])


class Word(Model):
    pos = CharField(choices=POS_CHOICES, max_length=15)
    spelling = CharField(max_length=255)
    definition = TextField()
    examples = TextField(blank=True)
    root = ForeignKey('Root', blank=True, null=True, related_name='derivatives')
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    '''
    gender = CharField(choices=GENDER_CHOICES, blank=True, max_length=15)
    human = CharField(choices=HUMAN_CHOICES, null=True, max_length=15)
    '''

    def get_absolute_url(self):
        return reverse_lazy('dictionary:word.detail', kwargs={'pk': self.pk, 'spelling': self.spelling})

    def __str__(self):
        return self.spelling