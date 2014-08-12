from django.views.generic import DetailView, ListView
from dictionary.models import Word, Deriver


class Search(ListView):
    model = Word
    template_name = 'word/search.html'
    context_object_name = 'results'

    def get_queryset(self):
        return self.model.objects.filter(**self.request.GET)


class WordDetail(DetailView):
    model = Word
    template_name = 'word/detail.html'


class DeriverDetail(DetailView):
    model = Deriver
    template_name = 'deriver/detail.html'