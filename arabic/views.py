from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from arabic.models import Word, Root
from arabic.utils import *


class Home(TemplateView):
    template_name = 'home.html'


home = Home.as_view()


def root(request, pk):
    return render(request, 'root.html', {'root': Root.objects.get(pk=pk)})


def word(request, pk):
    return render(request, 'word/word.html', {'word': Word.objects.get(pk=pk)})


class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'results'
    page_kwarg = 'page'

    def get_queryset(self):
        if self.request.REQUEST['language'] == 'ar':
            return Word.objects.filter(spelling__regex=('^' + ''.join(['(%s[%s]*)' % (i, TASHKEEL) for i in self.request.REQUEST['query']]) + '$'))
        elif self.request.REQUEST['language'] == 'en':
            return Word.objects.filter(definition__contains=self.request.REQUEST['query'])


search = Search.as_view()