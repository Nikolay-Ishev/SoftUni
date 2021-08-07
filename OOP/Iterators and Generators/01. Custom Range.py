class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.base = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            i = self.start
            self.start += 1
            return i
        else:
            self.start = self.base
            raise StopIteration()


one_ten = custom_range(1, 10)
for num in one_ten:
    print(num)

for num in one_ten:
    print(num + 1)
