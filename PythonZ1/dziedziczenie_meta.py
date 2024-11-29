class BaseClase:
    def base_method(self):
        return "Base method"
    
class DynamicMeta(type):
    def __new__(cls, name, bases, dct):
        if 'add_base' in dct:
            bases = bases + (BaseClase,)
        return super().__new__(cls, name, bases, dct)
    
class MyClass(metaclass=DynamicMeta):
    add_base = True

mc = MyClass()
print(mc.base_method())