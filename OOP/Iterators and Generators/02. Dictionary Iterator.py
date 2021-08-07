class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.counter = 0
        self.elements_list = list(dict_obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.dict_obj):
            i = self.counter
            self.counter += 1
            return self.elements_list[i]
        else:
            self.counter = 0
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
