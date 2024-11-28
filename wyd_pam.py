import sys

numbers = [i for i in range(10**6)]
print(f"Rozmiar listy: {sys.getsizeof(numbers)} bajtów")

numbers_gen = (i for i in range(10**6))
print(f"Rozmiar listy: {sys.getsizeof(numbers_gen)} bajtów")

for i in numbers_gen:
    print(i)

for i in numbers_gen:
    print(i)


def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data