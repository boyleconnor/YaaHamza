from arabic.models import Word, Root
from arabic.utils.ajax import ajax_hook


@ajax_hook
def word_detail(request):
    word = Word.objects.get(pk=request.POST['pk'])
    return word.__dict__


@ajax_hook
def root_detail(request):
    root = Root.objects.get(pk=request.POST['pk'])
    return root.__dict__


@ajax_hook
def search(request):
    return [Word.objects.search(**request.POST)]