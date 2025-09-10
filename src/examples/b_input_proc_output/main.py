from input_process_output import float_division

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = float_division(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")


if __name__ == "__main__":
    main()
