import tracemalloc


class LeakyClass:
    def __init__(self):
        self.data = [x for x in range(1000)]  # Alokacja dużej pamięci

leaks = []

tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

for _ in range(100):
    leaks.append(LeakyClass())  # Obiekty są przechowywane w globalnej liście

snapshot2 = tracemalloc.take_snapshot()
top_stats = snapshot2.compare_to(snapshot1, 'traceback')[:1]

print("[Zmiany w alokacji pamięci]")
print(tracemalloc.get_traced_memory())
for stat in top_stats[:10]:
    print(stat.traceback.format())


# objgraph.show_refs(leaks, max_depth=5, filename='refs.png')

tracemalloc.stop()