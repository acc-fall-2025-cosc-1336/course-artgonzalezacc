import unittest

from src.examples.b_input_proc_output.input_process_output import test_config, float_division

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_float_division(self):
        self.assertEqual(2, float_division(4,2))
        self.assertEqual(3.5, float_division(7,2))
        self.assertEqual(5, float_division(10,2))

