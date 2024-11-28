def dynamic_counter():
    counter = 0
    while True:
        value = yield counter
        if value is not None:
            counter = value
        else:
            counter += 1

gen = dynamic_counter()

print(next(gen))
print(gen.send(10))
print(next(gen))
print(gen.send(55))
print(next(gen))