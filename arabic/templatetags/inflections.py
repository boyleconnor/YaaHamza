from django.template import Library

register = Library()

@register.simple_tag
def get_inflections(word, **kwargs):
    lookup = str()
    for property_, value in kwargs.items():
        lookup += '(?=.*/%s:%s/)' % (property_, value)
    results = word.inflections.filter(properties__regex=lookup)
    if len(results) == 1:
        return results[0]
    elif len(results) > 1:
        return ' / '.join(results)
    return ''
