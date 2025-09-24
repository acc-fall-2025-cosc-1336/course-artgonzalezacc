import unittest

from src.examples.d_repetition.repetition import test_config, sum_to_n

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_to_n(self):
        self.assertEqual(6, sum_to_n(3))
        #self.assertEqual(10, sum_to_n(4))
        #self.assertEqual(15, sum_to_n(5))
        #self.assertEqual(55, sum_to_n(10))
        #self.assertEqual(5050, sum_to_n(100))

