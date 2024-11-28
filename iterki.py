# my_list = [1, 2, 3, 4, 5]

# my_iter = iter(my_list)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))  # StopIteration

class MyIter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.start - 1
        
# my_iter = MyIter(1, 5)
# for i in my_iter:
#     print(i)

def my_range(start, end):
    while start < end:
        yield start
        start += 1

for i in my_range(1, 5):
    print(i)