from project.student import Student
from unittest import TestCase, main


class StudentTest(TestCase):
    def setUp(self):
        self.student = Student("Test", {"course_1": [1, 2], "course_2": [3, 4]})
        self.student2 = Student("Test2")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student2.courses)
        self.assertEqual({"course_1": [1, 2], "course_2": [3, 4]}, self.student.courses)

    def test_enroll_when_course_name_already_exists(self):
        result_1 = self.student.enroll("course_1", [3, 4], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result_1)
        self.assertEqual({"course_1": [1, 2, 3, 4], "course_2": [3, 4]}, self.student.courses)

    def test_enroll_correct_with_add_course_notes_values(self):
        result_1 = self.student2.enroll("course_1", [3, 4], "Y")
        result_2 = self.student2.enroll("course_2", [5])
        self.assertEqual("Course and course notes have been added.", result_1)
        self.assertEqual("Course and course notes have been added.", result_2)
        self.assertEqual({"course_1": [3, 4], "course_2": [5]}, self.student2.courses)
        result_3 = self.student2.enroll("course_3", [6, 7], "NO")
        self.assertEqual("Course has been added.", result_3)
        self.assertEqual({"course_1": [3, 4], "course_2": [5], "course_3": []}, self.student2.courses)

    def test_add_notes_with_correct_course_name(self):
        self.assertEqual("Notes have been updated", self.student.add_notes("course_1", 3))
        self.assertEqual({"course_1": [1, 2, 3], "course_2": [3, 4]}, self.student.courses)

    def test_add_notes_raises_error_with_wrong_course_name(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes("course_1", 3)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_correct_course_name(self):
        self.assertEqual("Course has been removed", self.student.leave_course("course_1"))
        self.assertEqual({"course_2": [3, 4]}, self.student.courses)

    def test_leave_course_with_wrong_course_name(self):
        with self.assertRaises(Exception) as ex:
            self.student2.leave_course("course_2")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student2.courses)


if __name__ == "__main__":
    main()
