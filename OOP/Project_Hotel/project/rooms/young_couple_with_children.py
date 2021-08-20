from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.people.child import Child


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 30
        self.children = [ch for ch in children]
        self.members_count += len(self.children)
        self.appliances = []
        for el in range(2 + len(self.children)):
            self.appliances.append(Laptop())
            self.appliances.append(TV())
            self.appliances.append(Fridge())
        self.calculate_expenses(self.appliances, self.children)

# a = Child(2, 2)
# b = Child(2, 3)
# test_couple_ch = YoungCoupleWithChildren("Testovi", 1000, 2000, Child(2, 2), Child(2, 3))
# print(test_couple_ch.members_count)
# print(test_couple_ch.expenses)
# print(test_couple_ch.children)
# print(len(test_couple_ch.children))
# print(test_couple_ch.room_cost)
# print(test_couple_ch.budget)
# print(test_couple_ch.appliances)