import unittest

from src.examples.b_input_proc_output.input_process_output import integer_division, test_config, float_division, string_concatenation, string_concatenation_params

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

    def test_string_concatenation_no_params(self):
        self.assertEqual(string_concatenation(), "Hello World")

    def test_string_concatenation_params_basic(self):
        self.assertEqual(string_concatenation_params("Hello", "World"), "Hello World")

    def test_string_concatenation_params_empty(self):
        self.assertEqual(string_concatenation_params("", ""), " ")

    def test_string_concatenation_params_numbers(self):
        self.assertEqual(string_concatenation_params("123", "456"), "123 456")

    def test_string_concatenation_params_special_chars(self):
        self.assertEqual(string_concatenation_params("foo!", "@bar"), "foo! @bar")    


    

