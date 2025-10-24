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

    def test_list_shallow_copy(self):
        original_list = [10, 20, 30]
        copied_list = original_list
        
        original_list[0] = 99  # modify original_list to see if it affects "copied_list"
        
        self.assertNotEqual(copied_list, [10, 20, 30]) # since copied_list references the same list as original_list

    def test_list_deep_copy(self):
        original_list = [10, 20, 30]
        deep_copied_list = [] + original_list  # create a new list with the same elements
        
        original_list[0] = 99  # modify original_list to see if it affects deep_copied_list
        
        self.assertEqual(deep_copied_list, [10, 20, 30]) # deep_copied_list should remain unchanged


