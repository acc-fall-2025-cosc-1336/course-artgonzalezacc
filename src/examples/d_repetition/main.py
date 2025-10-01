from repetition import for_loop_break

def main():
    num = 0

    while num < 6 or num > 10:
        num = int(input("Enter a number for the multiplication table (6 to 10): "))

    for_loop_break(num, 3)

if __name__ == "__main__":
    main()

