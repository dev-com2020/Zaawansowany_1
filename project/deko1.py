def my_deco(func):
    def wrapper(*args, **kwargs):
        print(f'Before {func.__name__} z argumentami {args} i {kwargs}')
        result = func(*args, **kwargs)
        print(f'Zakończono {func.__name__}')
        return result
    return wrapper

@my_deco
def add(a,b):
    return a + b

add(2, 3)

# decorated_hello = my_deco(hello)
# decorated_hello()