import unittest

from rouna import rouna


class A:
    pass


class B:
    pass


class EqualsShould(unittest.TestCase):

    def test_return_true_for_class_with_identical_instance_variables(self):
        first_class = A()
        first_class.a = 1
        first_class.b = '2'

        second_class = B()
        second_class.b = '2'
        second_class.a = 1

        self.assertTrue(rouna.equals(first_class, second_class))

    def test_return_true_for_types_with_eq(self):
        self.assertTrue(rouna.equals(1, 1))
        self.assertTrue(rouna.equals('test_string', 'test_string'))
        self.assertTrue(rouna.equals([1,2,3], [1,2,3]))

    def test_return_false_for_class_with_not_identical_instance_variables(self):
        first_class = A()

        def first_method(self):
            return '1'
        first_class.a = first_method

        second_class = B()

        def second_method(self):
            return '1'

        second_class.a = second_method
        self.assertFalse(rouna.equals(first_class, second_class))

    def test_return_true_for_class_with_not_identical_instance_variables(self):
        first_class = A()

        def first_method(self):
            return '1'

        first_class.a = first_method

        second_class = B()

        second_class.a = first_method

        self.assertTrue(rouna.equals(first_class, second_class))
