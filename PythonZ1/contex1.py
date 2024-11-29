from contextlib import contextmanager

@contextmanager
def open_file(name,mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()


with open_file('test.txt', 'w') as f:
    f.write('Hello, world!')