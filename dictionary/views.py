from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from dictionary.forms import WordForm
from dictionary.models import Word, Root


class Search(ListView):
    def get_queryset(self):
        return []


class RootDetail(DetailView):
    model = Root
    template_name = 'root/detail.html'


class WordDetail(DetailView):
    model = Word
    template_name = 'word/detail.html'


class WordCreate(CreateView):
    model = Word
    form_class = WordForm
    template_name = 'word/edit.html'


class WordUpdate(UpdateView):
    model = Word
    form_class = WordForm
    template_name = 'word/edit.html'


class WordDelete(DeleteView):
    model = Word
    template_name = 'word/delete.html'
    success_url = reverse_lazy('home')