class MyContextManager:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter the context')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exititng the context')

    def __del__(self):
        print('deleting the object')

with MyContextManager() as manager:
    print('inside the context')