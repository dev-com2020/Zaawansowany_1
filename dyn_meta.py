attr = {
    'name': 'dyn_meta',
    'version': lambda self: f'name = {self.name}',
}

DynamicClass = type('DynamicClass', (object,), attr)

dyn_meta = DynamicClass()
print(dyn_meta.name)  # dyn_meta
print(dyn_meta.version())  # v0.1