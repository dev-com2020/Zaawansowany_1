import pickle

class SafeUnpickler(pickle.Unpickler):
    allowed_modules = {"MySafeClassxoxox","MySafeClass"}

    def find_class(self, module, name):
        if name not in self.allowed_modules:
            raise pickle.UnpicklingError('Attempting to unpickle unsafe module {}'.format(name))
        return super().find_class(module, name)

class MySafeClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "MySafeClass({})".format(self.value)
    
# data = pickle.dumps(MySafeClass(42))
# with open("data.pkl", "wb") as f:
#     f.write(data)

with open("data.pkl", "rb") as f:
    obj = SafeUnpickler(f).load()
    print(obj)
