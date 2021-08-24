class Planet:
    def __init__(self, name: str):
        self.name = name
        # an empty list of strings
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

