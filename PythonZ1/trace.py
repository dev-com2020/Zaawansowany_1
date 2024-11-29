import tracemalloc

class LeakyClass:
    def __init__(self):
        self.data = [x for x in range(1000000)]  # Alokacja dużej pamięci

leaks = []

tracemalloc.start()

for _ in range(10):
    leaks.append(LeakyClass())  # Obiekty są przechowywane w globalnej liście

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Top 10 lines]")
for stat in top_stats[:10]:
    print(stat)
