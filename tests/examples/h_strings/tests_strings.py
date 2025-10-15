import unittest

from src.examples.h_strings.strings import test_config, get_x_char_cnt_of_string, string_concatenation, is_substring_in_string, \
    is_substring_not_in_string

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_x_char_cnt_of_string(self):
        self.assertEqual(2, get_x_char_cnt_of_string("C++ is C++ and not Java", "C"))
        self.assertEqual(0, get_x_char_cnt_of_string("C++ is C++ and not Java", "X"))
        self.assertEqual(1, get_x_char_cnt_of_string("C++ is C++ and not Java", "J"))
        self.assertEqual(4, get_x_char_cnt_of_string("C++ is C++ and not Java", "+"))

    def test_string_concatenation(self):
        self.assertEqual("Hello World", string_concatenation("Hello ", "World"))
        self.assertEqual("12345", string_concatenation("12", "345"))
        self.assertEqual("!@#$%", string_concatenation("!@#", "$%"))
        self.assertEqual("Python3.8", string_concatenation("Python", "3.8"))

    def test_is_substring_in_string(self):
        self.assertTrue(is_substring_in_string("Hello World", "World"))
        self.assertFalse(is_substring_in_string("Hello World", "world")) #case sensitive
        self.assertTrue(is_substring_in_string("C++ is C++ and not Java", "C++"))
        self.assertFalse(is_substring_in_string("C++ is C++ and not Java", "JavaScript"))
        self.assertTrue(is_substring_in_string("Python3.8", "3.8"))
        self.assertFalse(is_substring_in_string("Python3.8", "3.9"))

    def test_is_substring_not_in_string(self):
        self.assertFalse(is_substring_not_in_string("Hello World", "World"))
        self.assertTrue(is_substring_not_in_string("Hello World", "world")) #case sensitive
        self.assertFalse(is_substring_not_in_string("C++ is C++ and not Java", "C++"))
        self.assertTrue(is_substring_not_in_string("C++ is C++ and not Java", "JavaScript"))
        self.assertFalse(is_substring_not_in_string("Python3.8", "3.8"))
        self.assertTrue(is_substring_not_in_string("Python3.8", "3.9"))