def data_source():
    value = int(input("Podaj liczbę (999 aby zakończyć): "))
    return value

# iterat = iter(data_source, 999)

# for i in iterat:
#     print(f"Otrzymana liczba: {i}")

def dyn_source(data_list):
    while data_list:
        yield data_list.pop(0)

data = [1, 2, 3, 4, 5]

ite = iter(dyn_source(data))

for i in ite:
    print(f"Otrzymana liczba: {i}")


data.extend([6, 7, 8, 9, 10])
ite = iter(dyn_source(data))
for i in ite:
    print(f"Otrzymana liczba: {i}")