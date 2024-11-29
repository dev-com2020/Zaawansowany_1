class RegistryMeta(type):
    
    registry = {}
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        if name != 'Base':
            cls.registry[name] = {
                "class": new_cls,
                "description": dct.get('type', 'No type')
            }
        return new_cls

class Base(metaclass=RegistryMeta):
    pass

class A(Base):
    type = 'A!!'


class B(Base):
    type = 'B!!'


for name,info in RegistryMeta.registry.items():
    print(name, info['description'])
    print(info['class'])