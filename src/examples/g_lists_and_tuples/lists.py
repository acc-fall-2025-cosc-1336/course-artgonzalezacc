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