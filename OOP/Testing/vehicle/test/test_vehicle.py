from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(fuel=50, horse_power=300)

    def test_init_creates_all_attributes(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(300, self.vehicle.horse_power)
        default_fuel_cons = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.assertEqual(default_fuel_cons, self.vehicle.fuel_consumption)

    def test_drive_decrease_correct_amount_of_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_drive_raises_error_when_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_adds_correct_amount(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)
        self.vehicle.refuel(10)
        self.assertEqual(47.5, self.vehicle.fuel)

    def test_refuel_raises_error_if_more_fuel_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_returns_correct_str(self):
        default_fuel_cons = Vehicle.DEFAULT_FUEL_CONSUMPTION
        result = f"The vehicle has 300 " \
                 f"horse power with 50 fuel left and {default_fuel_cons} fuel consumption"
        self.assertEqual(result, str(self.vehicle))


if __name__ == "__main__":
    main()
