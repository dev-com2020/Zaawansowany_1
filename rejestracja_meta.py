class RegistryMeta(type):
    
    _registry = {}
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        cls._registry[name] = new_cls
        return new_cls
    
class Base(metaclass=RegistryMeta):
    pass

class A(Base):
    pass

print(RegistryMeta._registry)  # {'Base': <class '__main__.Base'>, 'A': <class '__main__.A'>}