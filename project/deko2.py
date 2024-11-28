import time


def req_auth(func):
    def wrapper(user):
        if not user.get('is_logged_in'):
            raise PermissionError('Login required')
        return func(user)
    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start} seconds')
        return result
    return wrapper

@measure_time
def com(n):
    time.sleep(n)
    return n

# print(com(2))

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print('Hello')

say_hello()


class MyClass:
    @repeat(3)
    def method(self):
        print('Hello@@@')

obj = MyClass()
obj.method()