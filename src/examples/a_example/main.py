from devprocess import add_numbers

def main():
    num1 = input("Enter first number:  ")
    num2 = input("Enter second number: ")

    result = add_numbers(int(num1), int(num2))
    print("The sum is:", result)


if __name__ == "__main__":
    main()