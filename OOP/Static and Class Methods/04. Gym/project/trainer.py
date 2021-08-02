class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = self.__class__.id
        self.__class__.id += 1

    @staticmethod
    def get_next_id():
        return Trainer.id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"