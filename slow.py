import cProfile
from memory_profiler import profile

@profile
def slow_function():
    total = 0
    for _ in range(1000000):
        total += 1
    return total


# cProfile.run('slow_function()')
slow_function()
        