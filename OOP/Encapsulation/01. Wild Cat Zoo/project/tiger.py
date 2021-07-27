from project.animal import Animal


class Tiger(Animal):
# MONEY_FOR_CARE = 45 and put it in the super method (Lion.MONEY_FOR_CARE) instead of just value
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 45)

