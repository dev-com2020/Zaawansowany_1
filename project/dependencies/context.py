from contextlib import *
import urllib.request

@contextmanager
def custom_context():
    print('Entering custom context')
    try:
        yield "Resource"
    finally:
        print('Exiting custom context')

with custom_context() as resource:
    print('Inside custom context:', resource)


with closing(urllib.request.urlopen('http://www.google.com')) as page:
    print(page.read(100))

with suppress(ZeroDivisionError):
    print(1/0)

with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in ['file1.txt', 'file2.txt']]
    print(files)