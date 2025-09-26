def test_config():
    return True

def display_hello(num):
    counter = 0
    
    print('before loop')

    while counter < num:
        print(counter, num, counter < num, "Hello")
        counter = counter + 1
        if(counter > 2):
            print(counter, num, counter < num)

    print('after loop')

# function that sums values from 1 to n
def sum_to_n(n):
    total = 0
    counter = 0
    
    while counter <= n:
        total += counter #total = total + counter
        print(counter, n, counter <= n, total)
        counter += 1

        if(counter > n):
            print(counter, n, counter <= n, total)

    return total

def sum_of_squares(n):
    
    total = 0

    while n > 0:
        total += n * n #total = total + n * n
        print(n, n > 0, total)
        n -= 1

        if(n == 0):
            print(n, n > 0, total)

    return total

def display_hello_for_range(value):
    print('before loop')

    for num in range(0, value, 2):
        print(num, value, "Hello")

    print('after loop')

def sum_to_n_for(n):
    total = 0

    for counter in range(0, n + 1): # end range is n - 1
        total += counter #total = total + counter
        print(counter, n, counter <= n, total)

    return total

def sum_of_squares_for(n):
    total = 0

    for i in range(n, 0, -1):
        total += i * i #total = total + i * i
        print(i, i > 0, total)

    return total

def prompt_user():
    choice = 'y'

    while choice == 'y' or choice == 'Y':
        choice = input("Do you want to continue (y, n): ")
