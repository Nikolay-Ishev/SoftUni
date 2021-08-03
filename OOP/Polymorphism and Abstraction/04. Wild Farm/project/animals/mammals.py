from project.animals.animal import Mammal


class Mouse(Mammal):
    WEIGHT_INCR_PER_PC_OF_FOOD = 0.1

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ == "Vegetable" or food.__class__.__name__ == "Fruit":
            self.weight += Mouse.WEIGHT_INCR_PER_PC_OF_FOOD * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    WEIGHT_INCR_PER_PC_OF_FOOD = 0.4

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += Dog.WEIGHT_INCR_PER_PC_OF_FOOD * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    WEIGHT_INCR_PER_PC_OF_FOOD = 0.3

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ == "Vegetable" or food.__class__.__name__ == "Meat":
            self.weight += Cat.WEIGHT_INCR_PER_PC_OF_FOOD * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    WEIGHT_INCR_PER_PC_OF_FOOD = 1

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += Tiger.WEIGHT_INCR_PER_PC_OF_FOOD * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
