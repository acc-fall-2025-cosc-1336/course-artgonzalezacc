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