import itertools

numbers = range(10)
target_sum = 5

for r in range(2,len(numbers) + 1):
    for comb in itertools.combinations(numbers, r):
        if sum(comb) == target_sum:
            print(comb)