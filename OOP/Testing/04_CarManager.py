class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main

class CarTest(TestCase):
    def setUp(self):
        self.car = Car(make="Test", model="TestModel", fuel_consumption=5.6, fuel_capacity=100)

    def test_init(self):
        self.assertEqual("Test", self.car.make)
        self.assertEqual("TestModel", self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)

    def test_make_changes_or_raises_error_if_empty(self):
        self.car.make = "NewTest"
        self.assertEqual("NewTest", self.car.make)
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_changes_or_raises_error_if_empty(self):
        self.car.model = "NewTest"
        self.assertEqual("NewTest", self.car.model)
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_cons_changes_or_raises_error_if_negative(self):
        self.car.fuel_consumption = 6
        self.assertEqual(6, self.car.fuel_consumption)
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_changes_or_raises_error_if_negative(self):
        self.car.fuel_capacity = 6
        self.assertEqual(6, self.car.fuel_capacity)
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_changes_or_raises_error_if_negative(self):
        self.car.fuel_amount = 6
        self.assertEqual(6, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_add_fuel_or_raises_error_if_negative(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)
        self.car.refuel(1888)
        self.assertEqual(100, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_removes_correct_amount_or_raises_error_if_not_enough_fuel(self):
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel_amount)
        self.car.drive(100)
        self.assertEqual(94.4, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()