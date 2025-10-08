import unittest

from src.examples.e_functions.value_return_functions import test_config, generate_random_number

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_generate_random_number_range(self):
        start_range = 1
        end_range = 100

        for _ in range(start_range, end_range):
            num = generate_random_number(start_range, end_range)
            print(num)
            self.assertGreaterEqual(num, 1)
            self.assertLessEqual(num, 100)


    

