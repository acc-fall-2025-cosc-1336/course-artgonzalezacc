import unittest

from src.examples.h_strings.strings import test_config, get_x_char_cnt_of_string

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_x_char_cnt_of_string(self):
        self.assertEqual(2, get_x_char_cnt_of_string("C++ is C++ and not Java", "C"))
        self.assertEqual(0, get_x_char_cnt_of_string("C++ is C++ and not Java", "X"))
        self.assertEqual(1, get_x_char_cnt_of_string("C++ is C++ and not Java", "J"))
        self.assertEqual(4, get_x_char_cnt_of_string("C++ is C++ and not Java", "+"))

