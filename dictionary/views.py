from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models.base import get_absolute_url
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from dictionary.forms import WordForm, RootForm, InflectionForm
from dictionary.models import Word, Root, Inflection
from dictionary.utils.utils import search_pattern


class Home(TemplateView):
    template_name = 'home.html'


class RootDetail(DetailView):
    model = Root
    template_name = 'root/detail.html'


class RootCreate(CreateView):
    form_class = RootForm
    template_name = 'root/create.html'

    def get_success_url(self):
        return reverse_lazy('root-detail', kwargs={'pk': self.object.id})


class RootUpdate(UpdateView):
    model = Root
    form_class = RootForm
    template_name = 'root/update.html'


class RootDelete(DeleteView):
    model = Root
    form_class = RootForm
    template_name = 'root/delete.html'


class WordDetail(DetailView):
    model = Word
    template_name = 'word/detail.html'
    context_object_name = 'word'


class WordCreate(CreateView):
    form_class = WordForm
    template_name = 'word/create.html'

    def get_success_url(self):
        return reverse_lazy('word-detail', kwargs={'pk': self.object.id})


class WordUpdate(UpdateView):
    model = Word
    form_class = WordForm
    template_name = 'word/update.html'

    def get_success_url(self):
        return reverse_lazy('word-detail', kwargs={'pk': self.object.id})


class WordDelete(DeleteView):
    model = Word
    template_name = 'word/delete.html'
    success_url = reverse_lazy('home')


class WordSearch(ListView):
    """
    Search view for search results, by English or Arabic.
    """
    model = Word
    template_name = 'search.html'
    context_object_name = 'results'
    page_kwarg = 'page'
    paginate_by = 20

    def get_queryset(self):
        results = super().get_queryset()
        if not 'language' in self.request.GET or self.request.GET['language'] == 'ar':
            results = results.filter(spelling__regex=search_pattern(self.request.GET['query']))
        elif self.request.GET['language'] == 'en':
            results = results.filter(definition__contains=self.request.GET['query'])
        if 'pos' in self.request.GET:
            results = results.filter(pos=self.request.GET['pos'])
        return results