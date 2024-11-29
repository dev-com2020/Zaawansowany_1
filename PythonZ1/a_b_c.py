from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def do_something(self):
        pass

class B(A):
    # def do_something(self):
    #     print("Doing something")
    pass


b = B()
b.do_something()