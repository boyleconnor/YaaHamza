from django.views.generic import ListView, DetailView, TemplateView, CreateView
from arabic.models import Word, Root
from arabic.utils import *
from arabic.utils.utils import search_pattern


class Home(TemplateView):
    template_name = 'home.html'


class RootDetail(DetailView):
    model = Root
    template_name = 'root.html'


class WordDetail(DetailView):
    model = Word
    template_name = 'word/word_detail.html'
    context_object_name = 'word'


class WordCreate(CreateView):
    model = Word
    template_name = 'word/word_create.html'


class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'results'
    page_kwarg = 'page'

    def get_queryset(self):
        if self.request.GET['language'] == 'ar':
            return Word.objects.filter(spelling__regex=search_pattern(self.request.REQUEST['query']))
        elif self.request.GET['language'] == 'en':
            return Word.objects.filter(definition__contains=self.request.REQUEST['query'])
