from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_conditioner_consumption = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.air_conditioner_consumption) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_conditioner_consumption = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.air_conditioner_consumption) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)