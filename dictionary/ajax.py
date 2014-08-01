from django.shortcuts import get_object_or_404, get_list_or_404, render
from dictionary.models import Word, Root, Inflection
from dictionary.utils.ajax import jsonify


@jsonify
def root_detail(request):
    return get_object_or_404(Root, **request.GET.dict())


@jsonify
def root_list(request):
    return get_list_or_404(Root, **request.GET.dict())


@jsonify
def word_detail(request):
    return get_list_or_404(Word, **request.GET.dict())


def word_inflection_table(request, pk, tense_mood='indicative-imperfect'):
    word = get_object_or_404(Word, pk=pk)
    template = 'word/inflection_tables/'
    name = 'word'
    if word.pos == 'adjective':
        template += 'adjective_inflection_table.html'
        name = 'adjective'
    elif word.pos == 'noun':
        template += 'noun_inflection_table.html'
        name = 'noun'
    elif word.pos == 'verb':
        template += 'verb_inflection_table.html'
        name = 'verb'
    return render(request, template, {name: word, 'tense_mood': tense_mood})


@jsonify
def word_list(request):
    return get_list_or_404(Word, **request.GET.dict())


@jsonify
def inflection_detail(request):
    return get_object_or_404(Inflection, **request.GET.dict())


@jsonify
def inflection_list(request):
    return get_list_or_404(Inflection, **request.GET.dict())
