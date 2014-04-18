import json
import re
from django.db.models import Model, TextField, ForeignKey


class PropertyHolder(Model):
    """
    Abstract Model for models that have 'properties' <str>'s
    does NOT call self.save() when set_properties() is called
    """

    class Meta:
        abstract = True

    properties = TextField()

    def get_properties(self):
        """
        returns 'properties' TextField in form of python <dict>
        """
        if self.properties:
            return dict([tuple(i.split(':')) for i in self.properties.split('/')])
        else:
            return dict()

    def set_properties(self, properties):
        """
        sets properties <str> to given 'properties' <dict>
        """
        self.properties = '/'.join([':'.join(i) for i in properties.items()])


class Entry(Model):
    """
    Abstract Model for entries
    """

    class Meta:
        abstract = True

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
    template = TextField()

    def spell(self, origin):
        """
        :type self:
        """
        return re.compile(self.match).match(origin.spelling).expand(self.template)

    def apply(self):
        pass

    def __str__(self):
        return '%s : %s' % (self.match, self.template)


class Root(Entry):
    """
    Word root

    Ex: فعل, كتب, بسمل
    """
    definition = TextField()


class Word(Entry, PropertyHolder):
    """
    Model for fully-derived word

    Ex: مَطْبَخ, طَاَبِخ
    """
    definition = TextField()
    pos = TextField()
    root = ForeignKey('Root', blank=True, null=True, related_name='derivatives')
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    deriver = ForeignKey('Deriver', blank=True, null=True, related_name='words')

    def get_inflections(self, **kwargs):
        """
        Returns a string of all inflections matching the keywords, separated by a '/' where necessary
        """
        potential = [i.spelling for i in self.inflections.filter(**kwargs)]
        if len(potential) > 1:
            return potential[0]
        else:
            return potential.join(' / ')


class Inflection(Entry, PropertyHolder):
    """
    Model for fully-inflected word

    Ex: كِتَاَبُ, كُتُبْ
    """
    stem = ForeignKey(Word, related_name='inflections')
    inflecter = ForeignKey('Inflecter', blank=True, null=True, related_name='inflections')


class Deriver(Pattern, PropertyHolder):
    """
    Model for <Derivation> pattern
    """
    name = TextField()
    pos = TextField()

    def define(self, origin):
        return '(%s of %s)' % (self.name, origin)

    def apply(self, origin):
        """
        Creates (and saves to DB) <Word> model with:
            <spelling> - determined by <self.match> and <self.template> regex patterns
            <definition> - determined by <self.name> and <origin.spelling>
            <pos> - <self.pos>
            <deriver> - <self>
            <stem> - <origin> (if <origin> is a <Word>)
            <root> - <origin> (if <origin> is a <Root>)
        """
        return Word.objects.create(spelling=self.spell(origin), definition=self.define(origin), deriver=self,
                                   properties=self.properties, pos=self.pos,
                                   root=(origin if type(origin) == Root else origin.root),
                                   stem=(origin if type(origin) == Word else None))

    def __str__(self):
        return self.name


class Inflecter(Pattern, PropertyHolder):
    """
    Model for <Inflection> pattern
    """

    def apply(self, origin):
        return Inflection.objects.create(spelling=self.spell(origin), properties=self.properties, inflecter=self,
                                         stem=origin)