from repetition import nested_for_loop

def main():
    num = 0

    while num < 3 or num > 10:
        num = int(input("Enter a number for the nested for loop (3 to 10): "))

    nested_for_loop(num)

if __name__ == "__main__":
    main()

