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

    
    
