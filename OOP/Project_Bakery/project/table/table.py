from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.baked_food.bread import Bread


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.__capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        all_orders = self.drink_orders + self.food_orders
        result = 0
        for el in all_orders:
            result += el.price
        return result

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"



# table_1 = Table(2, 5)
# food_1 = Bread("hliab", 5)
#
# table_1.order_food(food_1)
# print(table_1.get_bill())
# print(table_1.free_table_info())
