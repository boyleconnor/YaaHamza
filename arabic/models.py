import re
from django.core.urlresolvers import reverse
from django.db.models import Model, TextField, ForeignKey, ManyToManyField
from django.db.models.manager import Manager
from arabic.utils.fields import PropertiesField
from arabic.utils.utils import search_pattern


class Entry(Model):
    """
    Abstract Model for entries
    """

    class Meta:
        abstract = True

    properties = PropertiesField()
    spelling = TextField()

    def __str__(self):
        return self.spelling


class Pattern(Model):
    """
    Abstract Model for patterns
    """

    class Meta:
        abstract = True

    match = TextField()
    spelling = TextField()
    properties = PropertiesField()

    def spell(self, origin):
        """
        :type self:
        """
        return re.compile(self.match).match(origin.spelling).expand(self.spelling)

    def apply(self, origin):
        pass

    def __str__(self):
        return '%s : %s' % (self.match, self.spelling)


class Root(Entry):
    """
    Word root

    Ex: فعل, كتب, بسمل
    """
    definition = TextField()


class Word(Entry):
    """
    Model for fully-derived word

    Ex: مَطْبَخ, طَاَبِخ
    """
    definition = TextField()
    pos = TextField()
    root = ForeignKey('Root', blank=True, null=True, related_name='derivatives')
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    pattern = ForeignKey('Deriver', blank=True, null=True, related_name='words')

    def get_inflections(self, **kwargs):
        """
        Returns a string of all inflections matching the keywords, separated by a '/' where necessary
        """
        potential = self.inflections.all()
        for (key, value) in kwargs.items():
            potential = potential.filter(properties__regex=('%s:%s' % (key, value)))
        potential = [i.spelling for i in potential]
        if len(potential) == 1:
            return potential[0]
        elif len(potential) > 1:
            return ' / '.join(potential)

    def get_absolute_url(self):
        return reverse('word-detail', kwargs={'pk': self.pk})


class Inflection(Entry):
    """
    Model for fully-inflected word

    Ex: كِتَاَبُ, كُتُبْ
    """
    stem = ForeignKey(Word, related_name='inflections')
    pattern = ForeignKey('Inflecter', blank=True, null=True, related_name='inflections')


class Deriver(Pattern):
    """
    Model for <Derivation> pattern
    """
    name = TextField()
    pos = TextField()
    inflecters = ManyToManyField('Inflecter', related_name='derivers')

    def define(self, origin):
        """
        Returns basic definition of the product of <self> and <origin>
        """
        return '(%s of %s)' % (self.name, origin)

    def apply(self, origin):
        """
        Creates (and saves to DB) <Word> model with:
            <spelling> - determined by <self.match> and <self.spelling> regex patterns using <self.spell()>
            <definition> - determined by <self.name> and <origin.spelling> using <self.define()>
            <pos> - <self.pos>
            <pattern> - <self>
            <stem> - <origin> (if <origin> is a <Word>)
            <root> - <origin> (if <origin> is a <Root>)
        """
        return Word.objects.create(spelling=self.spell(origin), definition=self.define(origin), pattern=self,
                                   properties=self.properties, pos=self.pos,
                                   root=(origin if type(origin) == Root else origin.root),
                                   stem=(origin if type(origin) == Word else None))

    def __str__(self):
        return self.name


class Inflecter(Pattern):
    """
    Model for <Inflection> pattern
    """

    def apply(self, origin):
        """
        Creates (and saves to DB) <Word> model with:
            <spelling> - determined by <self.match> and <self.spelling> regex patterns
            <definition> - determined by <self.properties>
            <properties> - <self.properties>
            <pattern> - <self>
            <stem> - <origin>
        """
        return Inflection.objects.create(spelling=self.spell(origin), properties=self.properties, pattern=self,
                                         stem=origin)