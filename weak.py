import weakref

class A:
    pass

a = A()
weak = weakref.ref(a)

print(weak())
del a
print(weak())