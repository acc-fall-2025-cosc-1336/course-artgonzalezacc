from repetition import multiplication_table_for

def main():
    num = 0

    while num < 3 or num > 10:
        num = int(input("Enter a number for the multiplication table (3 to 10): "))

    multiplication_table_for(num)

if __name__ == "__main__":
    main()

