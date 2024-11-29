class MetaA(type):
    pass

class MetaB(type):
    pass

class A(metaclass=MetaA):
    pass

class B(metaclass=MetaB):
    pass

class MetaCombined(MetaA, MetaB):
    pass

class C(A, B, metaclass=MetaCombined):
    pass