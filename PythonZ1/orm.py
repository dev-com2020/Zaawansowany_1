class ORMField:
    def __init__(self, field_type):
        self.field_type = field_type


class ORMModelMeta(type):
    def __new__(cls, name, bases, dct):
        fields = {k: v for k, v in dct.items() if isinstance(v, ORMField)}
        for k in fields:
            dct.pop(k)
        dct['_fields'] = fields
        return super().__new__(cls, name, bases, dct)
    
class BaseModel(metaclass=ORMModelMeta):
    pass

class User(BaseModel):
    name = ORMField("string")
    age = ORMField("integer")

print(User._fields)