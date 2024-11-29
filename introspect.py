obj = [1,2,3]
print(type(obj))
print(isinstance(obj, list))

class MyClass:
    def __init__(self):
        self.name = 'MyClass'

    def method(self):
        pass

instance = MyClass()
print(instance.__class__)
# print(dir(instance))

methods = [method for method in dir(instance) if callable(getattr(instance, method))]
# print(methods)

obj = MyClass()

print(hasattr(obj, 'name'))
print(getattr(obj, 'name'))
setattr(obj, 'name', 'new name')
delattr(obj, 'name')
print(getattr(obj, 'age', 'default value'))