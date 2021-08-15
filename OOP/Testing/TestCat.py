class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Test")

    def test_init(self):
        self.assertEqual("Test", self.cat.name)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)
        self.assertEqual(0, self.cat.size)

    def test_size_incr_after_eat(self):
        # Arrange
        self.assertEqual(0, self.cat.size)
        # Act
        self.cat.eat()
        # Assert
        self.assertEqual(1, self.cat.size)

    def test_fed_after_eat(self):
        # Arrange
        self.assertFalse(self.cat.fed)
        # Act
        self.cat.eat()
        # Assert
        self.assertTrue(self.cat.fed)

    def test_error_when_eat_after_fed(self):
        # Arrange
        self.assertFalse(self.cat.fed)
        # Act
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        # Assert
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_error_when_sleep_without_fed(self):
        # Arrange
        self.assertFalse(self.cat.fed)
        # Act and Assert
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_not_sleepy_after_sleep(self):
        # Arrange
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        # Act
        self.cat.sleep()
        # Assert
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
