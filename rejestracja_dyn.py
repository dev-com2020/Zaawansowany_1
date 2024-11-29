class RegistryMeta(type):
    
    registry = {}
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        if name != 'Base':
            cls.registry[dct.get('type',name)] = new_cls
        return new_cls

class Base(metaclass=RegistryMeta):
    pass

class A(Base):
    type = 'A'

    def handle(self):
        print('A')

class B(Base):
    type = 'B'

    def handle(self):
        print('B')

handler_type = 'A'
HandlerClass = RegistryMeta.registry[handler_type]
handler = HandlerClass()
print(handler.handle())