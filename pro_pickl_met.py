import pickle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._radius = 0

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def radius(self):
        return ("_radius", self._radius)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def __getstate__(self):
        return {"_radius": self._radius}

    def __setstate__(self, state):
        self._radius = state["_radius"]
    

r = Rectangle(10, 20)
serialied = pickle.dumps(r)
restored = pickle.loads(serialied)
print(restored.radius)  # ('_radius', 0)