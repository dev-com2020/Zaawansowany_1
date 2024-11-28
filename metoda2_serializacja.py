import gzip
import pickle


class SecureData:
    def __init__(self, data, public):
        self._data = data
        self.public = public

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_data']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._data = "odzyskano!"

# data = SecureData("tajne", "publiczne")
# serializowany = pickle.dumps(data)
# print(serializowany)

# restored = pickle.loads(serializowany)
# print(restored._data)

# data = {"tajne": "tajne", "publiczne": "publiczne"}

# with gzip.open('data.pkl.gz', 'wb') as f:
#     pickle.dump(data, f)

with gzip.open('data.pkl.gz', 'rb') as f:
    restored = pickle.load(f)
    print(restored)
