def test_config():
    return True

def list_indexing():
    #index  0  1  2  3   4
    nums = [2, 4, 6, 8, 10]
    print(nums[2])  # display 6
    print(nums[4])  # display 10

def loop_list_w_while():
    nums = [1, 3, 5, 7, 9]
    index = 0
    
    while index < len(nums):
        print(index, index < len(nums), len(nums), nums[index])
        index += 1

def loop_list_w_for_range():
    nums = [2, 4, 6, 8, 10]

    for index in range(len(nums)):
        print(index, len(nums), nums[index])

def loop_list_w_for():

    nums = [2, 4, 6, 8, 10]

    for num in nums:
        print(num)

def loop_update_element():
    nums = [1, 2, 3, 4, 5]

    print(nums)

    nums[2] = 0

    print(nums[2])#display updated element at index 2
    print(nums)

def list_holds_mixed_data_types():
    generic_list = [1, "two", 3.0, True]
    for item in generic_list:
        print(item)

def concatenate_lists():
    list_one = [1, 2, 3]
    list_two = [4, 5, 6]

    combined_list = list_one + list_two

    print(combined_list)

def list_as_parameter(my_list):
    my_list[0] = 10
    print(my_list)

def total_list_values_w_while(my_list):
    total = 0
    i = 0

    while i < len(my_list):
        total += my_list[i]
        i += 1
    
    return total

def average_list_values_w_for_range(my_list):
    total = 0

    for i in range(len(my_list)):
        total += my_list[i]
    
    average = total / len(my_list)
    
    return average

def list_sum_of_squares_w_for(my_list):
    sum_of_squares = 0

    for num in my_list:
        sum_of_squares += num ** 2

    return sum_of_squares

def return_list():
    return [1, 2, 3, 4, 5]
