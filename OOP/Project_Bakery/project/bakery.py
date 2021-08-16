from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        mapper = {"Bread": Bread, "Cake": Cake}
        if food_type == "Bread" or food_type == "Cake":
            for el in self.food_menu:
                if el.name == name:
                    raise Exception(f"{food_type} {name} is already in the menu!")
            self.food_menu.append(mapper[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        mapper = {"Tea": Tea, "Water": Water}
        if drink_type == "Tea" or drink_type == "Water":
            for el in self.drinks_menu:
                if el.name == name:
                    raise Exception(f"{drink_type} {name} is already in the menu!")
            self.drinks_menu.append(mapper[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        mapper = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}
        if table_type == "InsideTable" or table_type == "OutsideTable":
            for el in self.tables_repository:
                if el.table_number == table_number:
                    raise Exception(f"Table {table_number} is already in the bakery!")
            self.tables_repository.append(mapper[table_type](table_number, capacity))

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.reserve(number_of_people)
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        for table in self.tables_repository:
            not_in_the_menu = []
            if table.table_number == table_number:
                for food_name in args:
                    found = False
                    for available_food in self.food_menu:
                        if available_food.name == food_name:
                            table.order_food(available_food)
                            found = True
                            break
                    if not found:
                        not_in_the_menu.append(food_name)
                result_list = [repr(x) for x in table.food_orders]
                result1 = f"Table {table_number} ordered:\n" + "\n".join(result_list)
                result2 = f"\n{self.name} does not have in the menu:\n" + "\n".join(not_in_the_menu)
                return result1 + result2
        return f"Could not find table {table_number}"

    def order_drink(self, table_number, *args):
        for table in self.tables_repository:
            not_in_the_menu = []
            if table.table_number == table_number:
                for drink_name in args:
                    found = False
                    for available_drink in self.drinks_menu:
                        if available_drink.name == drink_name:
                            table.order_drink(available_drink)
                            found = True
                            break
                    if not found:
                        not_in_the_menu.append(drink_name)
                result_list = [repr(x) for x in table.drink_orders]
                result1 = f"Table {table_number} ordered:\n" + "\n".join(result_list)
                result2 = f"\n{self.name} does not have in the menu:\n" + "\n".join(not_in_the_menu)
                return result1 + result2
        return f"Could not find table {table_number}"

    def leave_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                self.total_income += bill
                table.clear()
                return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            result.append(table.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


test_bakery = Bakery("TestBakery")
test_bakery.add_food("Bread", "testbread", 2)
test_bakery.add_food("Bread", "testbread2", 2)
test_bakery.add_drink("Tea", "laika", 2, "niama")
test_bakery.add_drink("Tea", "mashterka", 2, "niama")
test_bakery.add_table("InsideTable", 1, 5)
test_bakery.add_table("InsideTable", 2, 5)
test_bakery.add_table("InsideTable", 3, 5)
print(test_bakery.order_food(1, "testbread", "testbread2", "nishto", "kartofi"))
print(test_bakery.order_drink(1, "laika", "mashterka"))
test_bakery.leave_table(1)
print(test_bakery.get_free_tables_info())
print(test_bakery.get_total_income())