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
        counter += 1

    return total

def sum_of_squares(n):
    
    total = 0

    while n > 0:
        total += n * n #total = total + n * n
        n -= 1

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

def display_menu():
    print("1. Sum to n")
    print("2. Sum of squares")
    print("3. Exit")

def run_menu():
    choice = ''
    
    while choice != '3':
        display_menu()
        choice = input("Enter your choice: ")
        print('')
        handle_choice(choice)
        print('')

def handle_choice(choice):
    if choice == '1':
        n = int(input("Enter a number to sum to: "))
        result = sum_to_n(n)
        print(f"Sum to {n} is {result}")
    elif choice == '2':
        n = int(input("Enter a number to sum squares to: "))
        result = sum_of_squares(n)
        print(f"Sum of squares to {n} is {result}")
    elif choice == '3':
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")

def nested_while_loop(n):
    i = 0
    while i < n:
        print(i, 'waiting on inner loop to finish')
        j = 0
        while j < n:
            print(i, j, '\tinner loop')
            j += 1
        i += 1

def multiplication_table(n):
    i = 0
    
    while i < n:
        j = 0
        while j < n:
            print(f"{(i+1) * (j+1):4}", end=' ')
            j += 1
        
        print()  # New line after each row
        i += 1

def nested_for_loop (n):
    for i in range(n):
        print(i, 'waiting on inner loop to finish')
        for j in range(n):
            print(i, j, '\tinner loop')