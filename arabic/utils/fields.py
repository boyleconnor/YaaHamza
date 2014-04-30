from django.db.models.fields import Field
from django.db.models.fields.subclassing import SubfieldBase


class DictField(Field, metaclass=SubfieldBase):
    pass
