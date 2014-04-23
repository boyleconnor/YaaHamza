from django.http import HttpResponse
from json import dumps as to_json


def ajax_hook(old_view):
    def new_view(*args, **kwargs):
        return HttpResponse(to_json(old_view(*args, **kwargs)))
    return new_view