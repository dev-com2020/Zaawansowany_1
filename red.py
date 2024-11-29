import pickle


class CustomClass:
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def create_instance(value):
        instance = CustomClass(value)
        instance.restored = True
        return instance
    
    def __reduce__(self):
        return (self.create_instance, (self.value,))
    

kl = CustomClass("Hello")
serialized = pickle.dumps(kl)
restored = pickle.loads(serialized)

print(restored.restored)