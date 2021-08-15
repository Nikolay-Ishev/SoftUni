class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


# Test if the worker is initialized with correct name, salary, and energy
# Test if the worker's energy is incremented after the rest method is called
# Test if an error is raised if the worker tries to work with negative energy or equal to 0
# Test if the worker's money is increased by his salary correctly after the work method is called
# Test if the worker's energy is decreased after the work method is called
# Test if the get_info method returns the proper string with correct values

import unittest


class WorkerTests(unittest.TestCase):
    # We can apply setUp method, remove all the rows where we create the same object and just call it with self.worker
    # def setUp(self):
    #     self.worker = Worker("Test", 100, 10)
    def test_worker_is_initialized_correctly(self):
        # Arrange and Act
        worker = Worker("Test", 100, 10)
        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_energy_increase_after_rest(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        # Act
        worker.rest()
        # Assert
        self.assertEqual(11, worker.energy)

    def test_error_when_works_with_negative_energy(self):
        # Arrange
        worker = Worker("Test", 100, 0)
        worker_2 = Worker("Test_2", 200, -10)
        # Act
        with self.assertRaises(Exception) as ex:
            worker.work()
            worker_2.work()
        # Assert
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_money_increased_correctly_after_work(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        self.assertEqual(0, worker.money)
        # Act
        worker.work()
        # Assert
        self.assertEqual(100, worker.money)

    def test_energy_decreased_after_work(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        # Act
        worker.work()
        # Assert
        self.assertEqual(9, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        # Act
        result = worker.get_info()
        expected_result = 'Test has saved 0 money.'
        # Assert
        self.assertEqual('Test has saved 0 money.', result)


if __name__ == "__main__":
    unittest.main()
