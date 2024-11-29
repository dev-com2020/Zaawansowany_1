from functools import lru_cache, partial, wraps
from dataclasses import dataclass

@lru_cache(maxsize=256)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# print(fib(209))

def multi(x, y):
    return x * y

double = partial(multi, 2)
# print(double(3))



def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args {args} and kwargs {kwargs}')
        return func(*args, **kwargs)
    return wrapper


@log_decorator
def add(x, y):
    return x + y

# print(add(2, 3))


@dataclass
class Person:
    name: str
    age: int

p = Person('John', 30)
print(p)