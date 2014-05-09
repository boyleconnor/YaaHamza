from django.shortcuts import get_object_or_404, get_list_or_404
from dictionary.models import Word, Root, Inflection
from dictionary.utils.ajax import ajax_hook


@ajax_hook
def root_detail(request):
    return get_object_or_404(Root, **request.GET.dict())


@ajax_hook
def root_list(request):
    return get_list_or_404(Root, **request.GET.dict())


@ajax_hook
def word_detail(request):
    return get_list_or_404(Word, **request.GET.dict())


@ajax_hook
def word_list(request):
    return get_list_or_404(Word, **request.GET.dict())


@ajax_hook
def inflection_detail(request):
    return get_object_or_404(Inflection, **request.GET.dict())


@ajax_hook
def inflection_list(request):
    return get_list_or_404(Inflection, **request.GET.dict())
