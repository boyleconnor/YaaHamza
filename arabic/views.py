from django.http import HttpResponse
from django.shortcuts import render
from arabic.models import Word, Root
from arabic.utils import *


def home(request):
    return render(request, 'home.html')


def root(request, pk):
    return render(request, 'root.html', {'root': Root.objects.get(pk=pk)})


def word(request, pk):
    return render(request, 'word/word.html', {'word': Word.objects.get(pk=pk)})


def search(request, q):
    pattern = '^'+''.join(['([%s][%s]*)' % (i, TASHKEEL) for i in q])+'$'
    results = list(Word.objects.filter(spelling__regex=pattern))
    return render(request, 'search.html', {'results': results, 'q': q})