import itertools
import operator

for i in itertools.count(start=10, step=2):
    if i > 20:
        break
    print(i)

kolory = ['czerwony', 'zielony', 'niebieski']
for i in itertools.cycle(kolory):
    print(i)

for i in itertools.repeat('Python', 3):
    print(i)

item = [1, 2, 3]
for perm in itertools.permutations(item, 2):
    print(perm)

for comb in itertools.combinations(item, 2):
    print(comb)

for comb in itertools.combinations_with_replacement(item, 2):
    print(comb)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for i in itertools.chain(list1, list2):
    print(i)

data = sorted([("a", 1), ("b", 2), ("c", 3)])
for key, group in itertools.groupby(data, lambda x: x[1]):
    print(key, list(group))

nums = [1, 2, 3, 4, 5]
result = itertools.accumulate(nums)
for i in result:
    print(i)

nums = [1, 2, 3, 4, 5]
result = itertools.accumulate(nums, operator.mul)
for i in result:
    print(i)

data = range(10)
result = itertools.islice(data, 2, 8, 2)
for i in result:
    print(i)

nums = [1, 2, 3, 4, 5]
for item in itertools.takewhile(lambda x: x < 4, nums):
    print(item)

for item in itertools.dropwhile(lambda x: x < 4, nums):
    print(item)