import re
from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, ForeignKey, CharField, TextField
from arabic_tools.constants import ABJAD
from dictionary.constants import POS_CHOICES


class Word(Model):
    pos = CharField(choices=POS_CHOICES, max_length=15)
    spelling = CharField(max_length=255)
    definition = TextField()
    examples = TextField(blank=True)
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    pattern = ForeignKey('Deriver', blank=True, null=True, related_name='words')

    def get_root(self):
        stem = self.stem
        if stem is None:
            return None
        elif stem.pos == 'root':
            return stem
        else:
            return stem.get_root()

    def get_detail_url(self):
        return reverse_lazy('dictionary:word.detail', kwargs={'pk': self.pk, 'spelling': self.spelling})
    '''
    def get_update_url(self):
        return reverse_lazy('dictionary:word.update', kwargs={'pk': self.pk, 'spelling': self.spelling})

    def get_delete_url(self):
        return reverse_lazy('dictionary:word.delete', kwargs={'pk': self.pk, 'spelling': self.spelling})
    '''
    def get_absolute_url(self):
        return self.get_detail_url()

    def __str__(self):
        return self.spelling


class Deriver(Model):
    origin_pos = CharField(choices=POS_CHOICES, max_length=15)
    result_pos = CharField(choices=POS_CHOICES, max_length=15)
    expectation = CharField(default=(('([%s])' % ABJAD) * 3), max_length=255)
    template = CharField(max_length=255)
    name = CharField(max_length=63, blank=True)

    def apply_spelling(self, word_in):
        if type(word_in) == str:
            spelling_in = word_in
        elif type(word_in) == Word:
            spelling_in = word_in.spelling
        else:
            raise TypeError('Type of ''word_in'' must be ''str'' or ''dictionary.word''')
        return re.match(self.expectation, spelling_in).expand(self.template)

    def apply(self, stem):
        return Word(spelling=self.apply_spelling(stem), pos=self.result_pos, stem=stem, pattern=self)

    def __str__(self):
        return self.name