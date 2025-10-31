import unittest

from src.examples.g_lists_and_tuples.lists import test_config, list_as_parameter, total_list_values_w_while, average_list_values_w_for_range, \
    list_sum_of_squares_w_for, return_list

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

    def test_append_to_list(self):
        nums = [1, 2, 3]
        nums.append(4)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_insert_into_list(self):
        nums = [1, 2, 4]
        nums.insert(2, 3)  # insert 3 at index 2
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_total_list_values_w_while(self):
        
        nums = [1, 2, 3, 4, 5]
        total = total_list_values_w_while(nums)
        self.assertEqual(total, 15)

    def test_average_list_values_w_for_range(self):
        nums = [2, 4, 6, 8, 10]
        average = average_list_values_w_for_range(nums)
        self.assertEqual(average, 6.0)

    def test_list_sum_of_squares_w_for(self):
        nums = [2, 4, 6 ]
        sum_of_squares = list_sum_of_squares_w_for(nums)
        self.assertEqual(sum_of_squares, 56)  # 2^2 + 4^2 + 6^2 = 56
    
    def test_return_list(self):
        nums = [1, 2, 3, 4, 5]
        returned_list = return_list()
        self.assertEqual(returned_list, nums)

    def test_return_list_is_new_instance(self):
        returned_list = return_list()
        another_list = return_list()
        self.assertIsNot(returned_list, another_list)  # Ensure they are different instances

        returned_list[0] = 100
        self.assertNotEqual(returned_list, another_list)  # Ensure modifying one does not affect the other

    def test_two_d_list_indexing(self):
        my_list = [[10,20,30], [40, 50, 60]] #hard coding

        self.assertEqual(10, my_list[0][0])
        self.assertEqual(50, my_list[1][1])

    def test_two_d_list_row_indexing(self):
        my_list = [[10,20,30], [40, 50, 60]]

        self.assertEqual([10,20,30], my_list[0])
        self.assertEqual([40,50,60], my_list[1])

    def test_create_two_d_list_w_code(self):
        my_list = [] #empty list
        first_row = []
        first_row.append(10)
        first_row.append(20)
        first_row.append(30) #list will be [10,20,30]

        self.assertEqual([10,20,30], first_row)

        my_list.append(first_row) #[[10,20,30]]

        self.assertEqual([[10,20,30]], my_list)

        second_row = []
        second_row.append(40)
        second_row.append(50)
        second_row.append(60)

        self.assertEqual([40,50,60], second_row)

        my_list.append(second_row)

        self.assertEqual([[10,20,30], [40, 50, 60]], my_list)
        


    


