class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
    
    @property
    def food(self):
        result = [x for x in self.supplies if x.__class__.__name__ == "FoodSupply"]
        if len(result) == 0:
            raise IndexError("There are no food supplies left!")
        return result
    
    @property
    def water(self):
        result = [x for x in self.supplies if x.__class__.__name__ == "WaterSupply"]
        if len(result) == 0:
            raise IndexError("There are no water supplies left!")
        return result

    @property
    def painkillers(self):
        result = [x for x in self.supplies if x.__class__.__name__ == "Painkiller"]
        if len(result) == 0:
            raise IndexError("There are no painkillers left!")
        return result

    @property
    def salves(self):
        result = [x for x in self.supplies if x.__class__.__name__ == "Salve"]
        if len(result) == 0:
            raise IndexError("There are no salves left!")
        return result

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            for med_i in range(-1, -len(self.medicine) - 1, -1):
                if self.medicine[med_i].__class__.__name__ == medicine_type:
                    self.medicine[med_i].apply(survivor)
                    del self.medicine[med_i]
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            for sust_i in range(-1, -len(self.supplies) - 1, -1):
                if self.supplies[sust_i].__class__.__name__ == sustenance_type:
                    self.supplies[sust_i].apply(survivor)
                    del self.supplies[sust_i]
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= (survivor.age * 2)
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")


from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve

bunker = Bunker()
sup = FoodSupply()
wat = WaterSupply()
pain = Painkiller()
salve = Salve()
bunker.supplies = [sup, sup, wat, wat, sup, wat]
bunker.medicine = [pain, salve, pain, salve, pain, salve]
print(bunker.food)
surv = Survivor("Test_name", 18)
surv_2 = Survivor("Test_name_2", 33)
bunker.add_survivor(surv)
bunker.add_survivor(surv_2)
bunker.next_day()
print(surv_2.needs_sustenance)
print(surv.needs_sustenance)
surv_2.health = 10
print(bunker.heal(surv_2, "Painkiller"))
print(bunker.heal(surv_2, "Painkiller"))
print(bunker.heal(surv_2, "Painkiller"))
print(bunker.heal(surv_2, "Painkiller"))
print(surv_2.health)
print([x.__class__.__name__ for x in bunker.medicine])
