class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = len(self.iterable) - 1
        self.base = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= 0:
            i = self.start
            self.start -= 1
            return self.iterable[i]
        else:
            self.start = self.base
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4, 5, 6, 200])
for item in reversed_list:
    print(item)