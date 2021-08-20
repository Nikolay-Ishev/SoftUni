class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for arg in args:
            for el in arg:
                result += el.get_monthly_expense()
        self.expenses = result


# from project.appliances.fridge import Fridge
# from project.people.child import Child
#
# test_fridge = Fridge()
# test_2_fridge = Fridge()
# test_child = Child(3, 2, 2)
# test_child_2 = Child(4, 1, 1)
# test_room = Room("test_room", 200, 5)
# print(test_child.get_monthly_expense())
# print(test_child_2.get_monthly_expense())
# print(test_fridge.get_monthly_expense())
# print(test_2_fridge.get_monthly_expense())
# test_room.calculate_expenses([test_child, test_child_2], [test_fridge, test_2_fridge])
# print(test_room.expenses)
