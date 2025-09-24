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