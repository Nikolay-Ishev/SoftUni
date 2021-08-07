class vowels:
    pattern = "AEOUYIaeouyi"

    def __init__(self, string):
        self.string = string
        self.start = 0
        self.vowels_list = [el for el in self.string if el in vowels.pattern]

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= len(self.vowels_list) - 1:
            i = self.start
            self.start += 1
            return self.vowels_list[i]
        else:
            self.start = 0
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
