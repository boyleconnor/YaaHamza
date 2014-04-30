from django.forms import ModelForm
from django.forms.widgets import TextInput
from arabic.models import Root, Inflection, Word


class RootForm(ModelForm):
    class Meta:
        model = Root
        fields = ['spelling', 'definition']
        widgets = {'spelling': TextInput()}


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['spelling', 'definition', 'pos', 'properties']
        widgets = {'spelling': TextInput()}


class InflectionForm(ModelForm):
    class Meta:
        model = Inflection
        fields = ['spelling', 'properties']
        widgets = {'spelling': TextInput()}
