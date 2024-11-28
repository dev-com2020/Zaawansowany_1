import pickle

data = {'a': [1, 2.0, 3, 4+6j],"age": 23}

# with open('data.pickle', 'wb') as f:
#     pickle.dump(data, f)

binary = pickle.dumps(data)
print(binary)

# with open('data.pickle', 'rb') as f:
#     data = pickle.load(f)
#     print(data)
#     print(type(data))
#     print(data['a'])
#     print(data['age'])

data = pickle.loads(binary)
print(data)