from django.core.exceptions import ValidationError
from django.db.models.fields import TextField
from django.db.models.fields.subclassing import SubfieldBase
from json import dumps, loads


class PropertiesField(TextField, metaclass=SubfieldBase):
    def __init__(self, *args, **kwargs):
        if 'possibilities' in kwargs:
            self.possibilities = kwargs['possibilities']
        else:
            self.possibilities = None
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        try:
            assert type(value) == dict
        except AssertionError:
            raise ValidationError("PropertiesField can only contain type 'dict'")
        return dumps(value)

    def value_to_string(self, obj):
        return dumps(obj)

    def to_python(self, value):
        if not value:
            return {}
        if type(value) == dict:  # TODO: Figure out why the hell this could ever be true (it always is).
            return value
        return loads(value)
