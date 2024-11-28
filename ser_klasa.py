import pickle

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User: {self.name}"
    
# user = User("John", "1234")
# with open("user.pkl", "wb") as f:
#     pickle.dump(user, f)

with open("user.pkl", "rb") as f:
    user = pickle.load(f)
    print(user)  # User: John