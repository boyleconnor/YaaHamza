from django.core.urlresolvers import reverse_lazy
from django.template import Library

register = Library()

@register.simple_tag
def get_inflections(word, **kwargs):
    results = word.inflections.filter(**kwargs)
    if len(results) == 1:
        return '<a href="%s">%s</a>' % (reverse_lazy('inflection-update', args=('pk', results[0].pk)), results[0])
    elif len(results) > 1:
        return ' / '.join(results)
    return '<i><a href="%s">Add</a>' % reverse_lazy()
