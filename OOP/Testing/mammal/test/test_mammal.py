from project.mammal import Mammal
from unittest import TestCase, main


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "cat", "meow")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_returns_correct_str(self):
        self.assertEqual("Test makes meow", self.mammal.make_sound())

    def test_get_kingdom_returns_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_correct_str(self):
        self.assertEqual("Test is of type cat", self.mammal.info())


if __name__ == "__main__":
    main()
