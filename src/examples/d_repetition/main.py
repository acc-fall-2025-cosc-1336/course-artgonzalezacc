from repetition import while_loop_continue

def main():
    num = 0

    while num < 6 or num > 10:
        num = int(input("Enter a number for the multiplication table (6 to 10): "))

    while_loop_continue(num, 3)

if __name__ == "__main__":
    main()

