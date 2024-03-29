class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.base = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 0:
            # self.number -= 1
            # if self.index < len(self.sequence):
            #     i = self.index
            #     self.index += 1
            #     return self.sequence[i]
            # else:
            #     self.index = 1
            #     return self.sequence[0]
            self.number -= 1
            i = self.index
            self.index += 1
            return self.sequence[i % len(self.sequence)]
        else:
            self.number = self.base
            raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')




