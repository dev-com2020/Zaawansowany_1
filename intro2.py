class MyClass:
    def powitanie(self):
        """Metoda zwracająca powitanie"""
        return "Witaj świecie!"
    
    def pozegnanie(self):
        return "Do zobaczenia!"


obiekt = MyClass()
methods = [method for method in dir(obiekt) if callable(getattr(obiekt, method)) and not method.startswith("__")]

for method_name in methods:
    method = getattr(obiekt, method_name)
    print(f'{method_name}: {method()}, {method.__doc__}')