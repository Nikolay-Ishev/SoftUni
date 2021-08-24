from project_test.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self):
        self.library = Library("TestName")

    def test_init_creates_all_attributes(self):
        self.assertEqual("TestName", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_value_error_when_empty(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_name_setter(self):
        self.library.name = "TestNameNew"
        self.assertEqual("TestNameNew", self.library.name)

    def test_add_book(self):
        self.library.add_book("test_author", "test_title")
        self.assertEqual({'test_author': ['test_title']}, self.library.books_by_authors)
        self.library.add_book("test_author", "test_title")
        self.assertEqual({'test_author': ['test_title']}, self.library.books_by_authors)

    def test_add_reader(self):
        self.library.add_reader("test_reader")
        self.assertEqual({'test_reader': []}, self.library.readers)
        self.assertEqual("test_reader is already registered in the TestName library.",
                         self.library.add_reader("test_reader"))

    def test_rent_book_if_reader_missing(self):
        self.assertEqual("test_reader is not registered in the TestName Library.",
                         self.library.rent_book("test_reader", "test_author", "test_title"))

    def test_rent_book_if_author_missing(self):
        self.library.add_reader("test_reader")
        self.assertEqual("TestName Library does not have any test_author's books.",
                         self.library.rent_book("test_reader", "test_author", "test_title"))

    def test_rent_book_if_book_missing(self):
        self.library.add_reader("test_reader")
        self.library.add_book("test_author", "test_title")
        self.assertEqual("TestName Library does not have test_author\'s \"test_title2\".",
                         self.library.rent_book("test_reader", "test_author", "test_title2"))

    def test_rent_book(self):
        self.library.add_reader("test_reader")
        self.library.add_book("test_author", "test_title")
        self.library.rent_book("test_reader", "test_author", "test_title")
        self.assertEqual({'test_author': []}, self.library.books_by_authors)
        self.assertEqual({'test_reader': [{'test_author': 'test_title'}]}, self.library.readers)

if __name__ == "__main__":
    main()
