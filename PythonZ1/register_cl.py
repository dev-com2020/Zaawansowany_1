registry = {}

def register_class(cls):
    registry[cls.__name__] = cls
    return cls

@register_class
class UserHandler:
    def handle(self):
        return 'UserHandler'
    
@register_class
class ProductHandler:
    def handle(self):
        return 'ProductHandler'
    
print(registry)

handler_type = 'UserHandler'
HandlerClass = registry[handler_type]
handler = HandlerClass()
print(handler.handle())