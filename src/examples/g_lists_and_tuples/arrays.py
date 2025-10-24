from array import array

def create_numeric_array():
    nums = array('i', [1, 2, 3, 4, 5]) # 'i' indicates an array of integers
    print(nums[1])

def loop_array_w_while():
    nums = array('i', [10, 20, 30, 40, 50])
    index = 0

    while index < len(nums):
        print(index, nums[index])
        index += 1

def loop_array_w_for_range():
    nums = array('f', [10.3, 20.5, 30.1, 40.2, 50.7]) # 'f' indicates an array of floats

    for index in range(len(nums)):
        print(index, nums[index])
