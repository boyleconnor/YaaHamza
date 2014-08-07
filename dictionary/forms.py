from django.forms import ModelForm
from dictionary.models import Word, Root


class RootForm(ModelForm):
    class Meta:
        model = Root
        fields = '__all__'


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'