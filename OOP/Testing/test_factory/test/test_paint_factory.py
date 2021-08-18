from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory
from project.factory.factory import Factory


class PaintFactoryTest(TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("TestName", 10)

    def test_init_creates_all_attributes(self):
        self.assertEqual("TestName", self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_add_ingredient(self):
        self.paint_factory.add_ingredient("blue", 5)
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual(self.paint_factory.ingredients["blue"], 5)
        self.assertEqual(self.paint_factory.ingredients["white"], 2)
        self.assertEqual(sum(self.paint_factory.ingredients.values()), 7)
        self.assertEqual(len(self.paint_factory.ingredients), 2)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("blue", 15)
        self.assertEqual("Not enough space in factory", str(ex.exception))
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("wrong", 2)
        self.assertEqual("Ingredient of type wrong not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient_with_correct_value(self):
        self.paint_factory.add_ingredient("blue", 5)
        self.paint_factory.remove_ingredient("blue", 5)
        self.assertEqual(0, self.paint_factory.ingredients["blue"])

    def test_remove_ingredient_wrong_value(self):
        self.paint_factory.add_ingredient("white", 2)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("wrong", 3)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_products(self):
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual({'white': 2}, self.paint_factory.products)

    def test_repr(self):
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual("Factory name: TestName with capacity 10.\nwhite: 2\n", repr(self.paint_factory))


if __name__ == "__main__":
    main()
