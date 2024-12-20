class SingleMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Single(metaclass=SingleMeta):
    def __init__(self):
        print('Single.__init__')

a = Single()
b = Single()
print(a is b)