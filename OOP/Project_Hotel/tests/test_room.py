from unittest import TestCase, main
from project.rooms.room import Room



class RoomTest(TestCase):
    def setUp(self):
        self.room = Room("Test_name", 1000.50, 4)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Test_name", self.room.family_name)
        self.assertEqual(1000.50, self.room.budget)
        self.assertEqual(4, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_props_raises_when_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_expenses_props_positive(self):
        self.room.expenses = 100
        self.assertEqual(100, self.room.expenses)

    def test_calculate_expenses(self):
        tv_test = TV()
        child_test = Child(5, 2)
        self.room.calculate_expenses([tv_test, tv_test], [child_test, child_test])
        self.assertEqual(510, self.room.expenses)


if __name__ == "__main__":
    main()
