class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print('Tworzenie klasy', name)
        dct['a'] = lambda self: print('Metoda a')
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('Inicjalizacja klasy', name)
        super().__init__(name, bases, dct)
    

class MyClass(metaclass=MyMeta):
    def b(self):
        print('Metoda b')


obj = MyClass()
print(obj.a())
print(obj.b())