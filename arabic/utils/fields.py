from django.db.models.fields.subclassing import SubfieldBase
from django import forms
from django.core import exceptions
from django.db import models
from django.utils.translation import ugettext_lazy as _


def dumps(value):
    value = dict(value)
    return '/'+'/'.join([':'.join(i) for i in value.items()])+'/'


def loads(value):
    value = value.strip('/')
    return dict([i.split(':') for i in value.split('/')])


class PropertiesField(models.Field, metaclass=SubfieldBase):
    description = _("Dictionary object")

    def get_internal_type(self):
        return "TextField"

    def to_python(self, value):
        if value is None:
            return None
        elif value == "":
            return {}
        elif isinstance(value, str):
            try:
                return dict(loads(value))
            except (ValueError, TypeError):
                raise exceptions.ValidationError(self.error_messages['invalid'])

        if isinstance(value, dict):
            return value
        else:
            return {}

    def get_prep_value(self, value):
        if not value:
            return ""
        elif isinstance(value, str):
            return value
        else:
            return dumps(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        return self.get_prep_value(value)

    def formfield(self, **kwargs):
        defaults = {'widget': forms.Textarea}
        defaults.update(kwargs)
        return super().formfield(**defaults)