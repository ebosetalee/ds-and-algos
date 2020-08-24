import unittest
from example.example import add, power


class TestExample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_two_arguments_must_be_supplied(self):
        with self.assertRaises(TypeError):
            add(1)

    def test_power(self):
        self.assertEqual(power(3, 2), 9)

    def test_power_number_should_not_be_negative(self):
        with self.assertRaises(TypeError):
            power(-1, 2)

    def test_power_exponent_should_not_be_negative(self):
        with self.assertRaises(TypeError):
            power(3, -4)
