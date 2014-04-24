from django.db.models.fields import CharField
from django.forms import ModelForm
from arabic.models import Root, Inflection, Word


class RootForm(ModelForm):
    class Meta:
        model = Root
        fields = ['spelling', 'definition']


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['spelling', 'definition', 'pos', 'properties']


class InflectionForm(ModelForm):
    class Meta:
        model = Inflection
        fields = ['spelling', 'properties']
