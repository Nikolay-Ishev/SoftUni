class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                new_budget = room.budget - total_expenses
                current_result = f"{room.family_name} paid {total_expenses:.2f}$ and have {new_budget:.2f}$ left."
                room.budget -= total_expenses
            else:
                current_result = f"{room.family_name} does not have enough budget and must leave the hotel."
                self.rooms.remove(room)
            result.append(current_result)
        return "\n".join(result)

    def status(self):
        all_people_in_the_hotel = 0
        result = []
        for room in self.rooms:
            all_people_in_the_hotel += room.members_count
            room_info = [f"{room.family_name} with {room.members_count} members."
                         f" Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"]
            if room.children:
                n = 1
                appliances = room.expenses
                for child in room.children:
                    room_info.append(f"--- Child {n} monthly cost: {child.get_monthly_expense():.2f}$")
                    n += 1
                    appliances -= child.get_monthly_expense()
            else:
                appliances = room.expenses
            room_info.append(f"--- Appliances monthly cost: {appliances:.2f}$")
            result.append("\n".join(room_info))
        return f"Total population: {all_people_in_the_hotel}\n" + "\n".join(result)


# from rooms.young_couple import YoungCouple
# from rooms.young_couple_with_children import YoungCoupleWithChildren
# from people.child import Child
#
# everland = Everland()
#
# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())
#
#
# if __name__ == "__main__":
#     test_one()