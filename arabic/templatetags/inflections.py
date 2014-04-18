from django.template import Library

register = Library()

@register.simple_tag
def get_inflections(word, **kwargs):
    return word.get_inflections(**kwargs)
