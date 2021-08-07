class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.count:
            i = self.start
            self.start += 1
            return self.step * i
        else:
            self.start = 0
            raise StopIteration

