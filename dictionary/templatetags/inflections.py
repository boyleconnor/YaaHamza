from django.template import Library

register = Library()

@register.simple_tag
def get_inflections(word, **kwargs):
    results = word.inflections.filter(**kwargs)
    if len(results) == 1:
        return results[0]
    elif len(results) > 1:
        return ' / '.join(results)
    return ''
