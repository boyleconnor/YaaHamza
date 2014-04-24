from django.views.generic import ListView, DetailView, TemplateView, CreateView
from arabic.models import Word, Root


class Home(TemplateView):
    """
    View for landing page
    """
    template_name = 'home.html'


class RootDetail(DetailView):
    """
    Detail view for Root
    """
    model = Root
    template_name = 'root.html'


class WordDetail(DetailView):
    """
    Detail view for Word
    """
    model = Word
    template_name = 'word/word_detail.html'
    context_object_name = 'word'


class WordCreate(CreateView):
    #TODO: implement
    model = Word
    template_name = 'word/word_create.html'


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
