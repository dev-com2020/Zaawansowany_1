import tracemalloc

class MyClass:
    def __init__(self):
        self.data = [x for x in range(1000)]

tracemalloc.start()

instances = [MyClass() for _ in range(100)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.filter_traces((
    tracemalloc.Filter(False, "<frozen importlib"),  # Ignorowanie importów
))

print("[Statystyki pamięci]")
for stat in top_stats[:10]:
    print(stat)
