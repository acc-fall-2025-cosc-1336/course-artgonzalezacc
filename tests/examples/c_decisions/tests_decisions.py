import unittest

from src.examples.c_decisions.decisions import test_config, is_even, compare_strings, is_number_in_range, is_number_not_in_range

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
        self.assertTrue(is_even(-4))

    def test_is_odd(self):
        from src.examples.c_decisions.decisions import is_odd
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(-1))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(0))
        self.assertTrue(is_odd(-5))

    def test_is_vowel(self):
        from src.examples.c_decisions.decisions import is_vowel
        self.assertTrue(is_vowel('a'))
        self.assertTrue(is_vowel('e'))
        self.assertTrue(is_vowel('i'))
        self.assertTrue(is_vowel('o'))
        self.assertTrue(is_vowel('u'))
        self.assertFalse(is_vowel('b'))
        self.assertFalse(is_vowel('z'))
        self.assertFalse(is_vowel('w')) 

    def test_compare_strings(self):
        self.assertTrue(compare_strings('hello', 'hello'))
        self.assertFalse(compare_strings('hello', 'world'))
        self.assertTrue(compare_strings('', ''))
        self.assertFalse(compare_strings('Python', 'python'))

    def test_is_number_in_range(self):
        self.assertTrue(is_number_in_range(5, 1, 10))
        self.assertTrue(is_number_in_range(1, 1, 10))
        self.assertTrue(is_number_in_range(10, 1, 10))
        self.assertFalse(is_number_in_range(0, 1, 10))
        self.assertFalse(is_number_in_range(11, 1, 10))
        self.assertTrue(is_number_in_range(-5, -10, 0))
        self.assertFalse(is_number_in_range(-11, -10, 0))
        self.assertFalse(is_number_in_range(1, 2, 3))

    def test_is_number_not_in_range(self):
        self.assertFalse(is_number_not_in_range(5, 1, 10))
        self.assertFalse(is_number_not_in_range(1, 1, 10))
        self.assertFalse(is_number_not_in_range(10, 1, 10))
        self.assertTrue(is_number_not_in_range(0, 1, 10))
        self.assertTrue(is_number_not_in_range(11, 1, 10))
        self.assertFalse(is_number_not_in_range(-5, -10, 0))
        self.assertTrue(is_number_not_in_range(-11, -10, 0))
        self.assertTrue(is_number_not_in_range(1, 2, 3))



