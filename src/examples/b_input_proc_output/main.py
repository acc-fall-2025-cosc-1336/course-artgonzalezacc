from input_process_output import integer_division

def main():
    a = int(input("Enter first integer: "))#input convert to int(whole number)
    b = int(input("Enter second integer: "))

    print("Integer division:", integer_division(a, b))
    

if __name__ == "__main__":
    main()
