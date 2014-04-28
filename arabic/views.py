from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models.base import get_absolute_url
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from arabic.forms import WordForm
from arabic.models import Word, Root


class Home(TemplateView):
    template_name = 'home.html'


class RootDetail(DetailView):
    model = Root
    template_name = 'root/detail.html'


class WordDetail(DetailView):
    """
    Detail view for Word
    """
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


class Search(ListView):
    """
    List view for search results, by English or Arabic.
    """
    template_name = 'search.html'
    context_object_name = 'results'
    page_kwarg = 'page'
    paginate_by = 20

    def get_queryset(self):
        return Word.objects.search(**self.request.GET.dict())
