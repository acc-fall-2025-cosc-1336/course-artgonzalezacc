import unittest

from datetime import datetime

from src.examples.e_functions.value_return_functions import test_config, generate_random_number, generate_random_number_with_seed

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_generate_random_number_range(self):
        start_range = 1
        end_range = 100

        for _ in range(start_range, end_range):
            num = generate_random_number(start_range, end_range)
            self.assertGreaterEqual(num, 1)
            self.assertLessEqual(num, 100)

    def test_generate_random_number_with_seed(self):
        start_range = 1
        end_range = 100
        now = datetime.now()
        seed = int(now.timestamp() * 1000) #set it to the current time in milliseconds
        #seed = 42 #set it to the current time in milliseconds

        for _ in range(start_range, end_range):
            num1 = generate_random_number_with_seed(start_range, end_range, seed)

            num2 = generate_random_number_with_seed(start_range, end_range, seed)

            self.assertEqual(num1, num2)

    
