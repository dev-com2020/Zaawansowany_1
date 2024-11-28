def data_validator():
    while True:
        data = yield
        if isinstance(data, int) and data > 0:
            print(f"Data is valid: {data}")
        else:
            print(f"Data is invalid: {data}")

val = data_validator()
next(val)
val.send(-10)
val.send(10)
val.send("abc")