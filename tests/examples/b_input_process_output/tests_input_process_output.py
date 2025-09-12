import unittest

from src.examples.b_input_proc_output.input_process_output import integer_division, test_config, float_division

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_float_division(self):
        self.assertEqual(2, float_division(4,2))
        self.assertEqual(3.5, float_division(7,2))
        self.assertEqual(5, float_division(10,2))

    def test_integer_division(self):
        self.assertEqual(2, integer_division(5,2))
        self.assertEqual(3, integer_division(7,2))
        self.assertEqual(5, integer_division(10,2))

