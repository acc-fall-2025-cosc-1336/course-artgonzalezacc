import unittest

from src.examples.g_lists_and_tuples.lists import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_if_new_list_created_in_concatenate_lists(self):
        list_one = [1, 2, 3]
        list_two = [4, 5, 6]
        combined_list = list_one + list_two
        
        list_one[1] = 99  # modify list_one to see if it affects combined_list
        list_two[1] = 88  # modify list_two to see if it affects combined_list
        
        self.assertEqual(combined_list, [1, 2, 3, 4, 5, 6])

