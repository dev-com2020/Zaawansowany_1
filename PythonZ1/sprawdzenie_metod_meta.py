class ValidationMeta(type):
    def __new__(cls, name, bases, dct):
        # Sprawdź, czy klasa implementuje wymagane metody
        required_methods = ['validate', 'process']
        for method in required_methods:
            if method not in dct:
                raise TypeError(f"Class {name} must implement method {method}")
        return super().__new__(cls, name, bases, dct)
    
class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        # Tworzymy klasę
        new_class = super().__new__(cls, name, bases, dct)
        # Rejestrujemy klasę, o ile to nie jest klasa bazowa
        if name != "BaseClass":
            cls.registry[name] = new_class
        return new_class
    
class AddMethodMeta(type):
    def __new__(cls, name, bases, dct):
        # Dodajemy metodę do każdej klasy
        dct['greet'] = lambda self: f"Hello from {name}"
        return super().__new__(cls, name, bases, dct)
    
class DynamicMeta(type):
    def __new__(cls, name, bases, dct):
        # Dodanie dynamicznego atrybutu
        dct['dynamic_attribute'] = f"Dynamic value for {name}"
        return super().__new__(cls, name, bases, dct)
    
