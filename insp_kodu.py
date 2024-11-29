import inspect
import types

def my_func():
    print("Hello")

def my_func2(a,b,c=19):
    pass

class Parennt:
    def __init__(self,a):
        self.a = a

class Child(Parennt):
    def __init__(self):
        pass


# print(inspect.getsource(my_func))
# print(inspect.signature(my_func2))

# print(inspect.getsource(Parennt))
# print(inspect.signature(Parennt))

# print(inspect.getsource(Child))
# print(inspect.signature(Child))
print(inspect.getmro(Child))

print(isinstance(my_func, types.FunctionType))