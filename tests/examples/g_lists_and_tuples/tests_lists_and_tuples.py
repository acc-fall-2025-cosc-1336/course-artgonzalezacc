import unittest

from src.examples.g_lists_and_tuples.lists import test_config, list_as_parameter

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

    def test_list_as_parameter(self):
        my_list = [1, 2, 3]
        expected_list = [10, 2, 3]
        list_as_parameter(my_list)
        self.assertEqual(my_list[0], expected_list[0])  # the first element should be updated to 10
        self.assertEqual(my_list, expected_list)  # the entire list should match the expected list

    def test_search_in_list(self):
        nums = [5, 10, 15, 20, 25]
        target = 15
        found = False

        if target in nums:
            found = True

        self.assertTrue(found)

    def test_search_not_in_list(self):
        nums = [5, 10, 15, 20, 25]
        target = 30
        not_in_list = True

        if target not in nums:
            not_in_list = False

        self.assertFalse(not_in_list)

