from django.forms import ModelForm
from django.forms.widgets import TextInput, Select
from dictionary.models import Root, Inflection, Word


class RootForm(ModelForm):
    class Meta:
        model = Root
        fields = ['spelling', 'definition']
        widgets = {'spelling': TextInput(), 'definition': TextInput()}


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['spelling', 'definition', 'pos', 'gender', 'root']
        widgets = {'spelling': TextInput(), 'definition': TextInput(), 'pos': Select(), 'gender': Select()}


class InflectionForm(ModelForm):
    class Meta:
        model = Inflection
        fields = ['spelling', 'gender', 'state', 'count', 'person', 'tense_mood', 'case']
        widgets = {'spelling': TextInput(), 'gender': Select(), 'state': Select(), 'count': Select(),
                   'person': Select(), 'tense_mood': Select(), 'case': Select()}
