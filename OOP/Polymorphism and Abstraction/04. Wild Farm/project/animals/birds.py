from project.animals.animal import Bird


class Owl(Bird):
    WEIGHT_INCR_PER_PC_OF_FOOD = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += Owl.WEIGHT_INCR_PER_PC_OF_FOOD * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    WEIGHT_INCR_PER_PC_OF_FOOD = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += Hen.WEIGHT_INCR_PER_PC_OF_FOOD * food.quantity
        self.food_eaten += food.quantity
