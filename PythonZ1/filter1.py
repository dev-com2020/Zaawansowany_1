import tracemalloc

tracemalloc.start()

snapshot = tracemalloc.take_snapshot()
stats = snapshot.filter_traces((
    tracemalloc.Filter(inclusive=True, filename_pattern="*my_module*"),
))

print("[ Top 10 ]")
for stat in stats[:10]:
    print(stat)