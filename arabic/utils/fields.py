from django.core.exceptions import FieldError
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

    def __init__(self, *args, **kwargs):
        if 'possibilities' in kwargs:
            self.possibilities = kwargs.pop('possibilities')
        else:
            raise FieldError("PropertiesField must be called with parameter 'possibilities'")
        super().__init__(*args, **kwargs)

    def get_internal_type(self, *args, **kwargs):
        return "TextField"

    def validate(self, value, model_instance):
        if isinstance(value, dict):
            for i in value:
                if i not in self.possibilities:
                    raise exceptions.ValidationError('%s is not a possible property' % (i,))
                if value[i] not in self.possibilities[i]:
                    raise exceptions.ValidationError('%s not in possible %s values' % (value[i], i))
        elif isinstance(value, str):
            for i in value.split('/'):
                prop, val = i.split(':')
                if prop not in self.possibilities:
                    raise exceptions.ValidationError()
                if val not in self.possibilities[prop]:
                    raise exceptions.ValidationError('%s not in possible %s values' % (val, prop))
        return super().validate(value, model_instance)

    def to_python(self, value):  # TODO: A bunch of this can be cut out but it is really easy to break
        if value is None:
            result = None
        elif value == "":
            result = {}
        elif isinstance(value, str):
            try:
                result = dict(loads(value))
            except (ValueError, TypeError):
                raise exceptions.ValidationError(self.error_messages['invalid'])

        if isinstance(value, dict):
            result = value
        else:
            result = {}
        return result

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