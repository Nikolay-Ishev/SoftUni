class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class ListTest(TestCase):
    def setUp(self):
        self.int_list = IntegerList(1, 2, 3)

    def test_init(self):
        self.assertEqual([1, 2, 3], self.int_list._IntegerList__data)

    def test_init_takes_only_integers(self):
        int_list = IntegerList(1.5, "test", False)
        self.assertEqual([], int_list._IntegerList__data)

    def test_add_int_is_added(self):
        self.assertEqual([1, 2, 3, 4], self.int_list.add(4))

    def test_error_when_add_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.add("Test")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_removes_and_returns_el_by_i(self):
        self.assertEqual(2, self.int_list.remove_index(1))
        self.assertEqual([1, 3], self.int_list._IntegerList__data)

    def test_remove_index_error_when_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))
        # with self.assertRaises(IndexError) as ex:
        #     self.int_list.remove_index(-1)
        # self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_returns_right_el_by_i(self):
        self.assertEqual(2, self.int_list.get(1))

    def test_get_index_out_of_range_error(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_i_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(3, 3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_not_int_error(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(2, "test")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert(self):
        self.int_list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3], self.int_list.get_data())

    def test_get_biggest(self):
        self.assertEqual(3, self.int_list.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.int_list.get_index(1))


if __name__ == "__main__":
    main()
