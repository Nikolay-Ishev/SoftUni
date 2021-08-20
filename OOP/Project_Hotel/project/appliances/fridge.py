from project.appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self):
        super().__init__(1.2)




# test = Fridge()
# print(test.get_monthly_expense())