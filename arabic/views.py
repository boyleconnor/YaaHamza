from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse
from django.shortcuts import render, redirect
from arabic.models import Word, Root
from django.db.models import ObjectDoesNotExist
from arabic.constants import ROOT_LENGTHS, ABJAD, TASHKEEL


def home(request):
    return HttpResponse("Hello, world!")


def root(request, pk):
    return render(request, 'root.html', {'root': Root.objects.get(pk=pk)})


def word(request, pk):
    return render(request, 'word.html', {'word': Word.objects.get(pk=pk)})


def search(request, q):
    pattern = '^'+''.join(['([%s][%s]*)' % (i, TASHKEEL) for i in q])+'$'
    results = list(Word.objects.filter(spelling__regex=pattern))
    return render(request, 'search.html', {'results': results, 'q': q})