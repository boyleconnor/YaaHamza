import re
from arabic.utils.constants import WORD_PROPERTIES, INFLECTION_PROPERTIES
from django.core.urlresolvers import reverse
from django.db.models import Model, TextField, ForeignKey, ManyToManyField
from arabic.utils.fields import PropertiesField


class Root(Model):
    """
    Word root

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
    pos = TextField()
    properties = PropertiesField(possibilities=WORD_PROPERTIES)
    root = ForeignKey('Root', blank=True, null=True, related_name='derivatives')
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    pattern = ForeignKey('Deriver', blank=True, null=True, related_name='words')

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
    properties = PropertiesField(possibilities=INFLECTION_PROPERTIES)
    stem = ForeignKey(Word, related_name='inflections')
    pattern = ForeignKey('Inflecter', blank=True, null=True, related_name='inflections')

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

    def spell(self, origin):
        return re.compile(self.match).match(origin.spelling).expand(self.spelling)

    def apply(self, origin):
        pass

    def __str__(self):
        return '%s : %s' % (self.match, self.spelling)


class Deriver(Pattern):
    """
    Model for <Derivation> pattern
    """
    name = TextField()
    pos = TextField()
    inflecters = ManyToManyField('Inflecter', related_name='derivers')
    properties = PropertiesField(possibilities=WORD_PROPERTIES)

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

    properties = PropertiesField(possibilities=INFLECTION_PROPERTIES)

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