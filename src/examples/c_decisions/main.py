from decisions import is_number_in_range

def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    num = int(input("Enter a number to check: "))

    if is_number_in_range(num, start, end):
        print(f"The number {num} is in the range {start} to {end}.")
    else:
        print(f"The number {num} is not in the range {start} to {end}.")

if __name__ == "__main__":
    main()
