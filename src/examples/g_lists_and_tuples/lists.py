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
        print(nums[index])
        index += 1

def loop_list_w_for_range():
    nums = [2, 4, 6, 8, 10]

    for index in range(len(nums)):
        print(index, len(nums), nums[index])