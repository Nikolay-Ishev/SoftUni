class Stack:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if any(self.data):
            return False
        return True

    def __str__(self):
        return "[" + f"{', '.join(reversed(self.data))}" + "]"


a = Stack(["a", "v"])
print(a)
