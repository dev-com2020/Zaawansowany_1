import pickle
import hashlib

def create_secure_hash(data, file_path, secret_key):
    serialized_data = pickle.dumps(data)
    hash_value = hashlib.sha256(serialized_data + secret_key).hexdigest()

    with open(file_path, 'wb') as f:
        f.write(hash_value.encode('utf-8') + b'\n' + serialized_data)

def load_secure_hash(file_path, secret_key):
    with open(file_path, 'rb') as f:
        stored_value = f.readline().strip().decode('utf-8')
        serialized_data = f.read()

    calculated_value = hashlib.sha256(serialized_data + secret_key).hexdigest()
    if stored_value != calculated_value:
        raise ValueError('Data has been tampered with!')

    return pickle.loads(serialized_data)

# Przykład użycia
data = {'name': 'John', 'age': 30}
secret_key = b'my_secret_key'

create_secure_hash(data, 'secure.pickle', secret_key)
loaded_data = load_secure_hash('secure.pickle', secret_key)

print(loaded_data)  # {'name': 'John', 'age': 30}
    
