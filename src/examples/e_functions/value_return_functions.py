from random import randint

def test_config():
    return True

def return_hello():
    return 'hello'

def say_hello(name='C++'):
    print('hello ' + name)

def generate_random_number(start_range, end_range):
    return randint(start_range, end_range)

def generate_random_number_with_seed(start_range, end_range, seed):
    from random import seed as set_seed
    set_seed(seed)
    return randint(start_range, end_range)

def get_dice_roll():
    return randint(1, 6)