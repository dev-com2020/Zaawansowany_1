class ValidateMeta(type):
    def __new__(cls, name, bases, dct):
        if 'validate' not in dct:
            raise ValueError('validate method is required')
        return super().__new__(cls, name, bases, dct)
    
class Base(metaclass=ValidateMeta):
    def validate(self):
        pass