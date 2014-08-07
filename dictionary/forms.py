from django.forms import ModelForm
from dictionary.models import Word


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'