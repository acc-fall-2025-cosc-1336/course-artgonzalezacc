from repetition import nested_while_loop

def main():
    num = 0

    while num < 1 or num > 5:
        num = int(input("Enter a number for nested loops(1 to 5): "))

    nested_while_loop(num)

if __name__ == "__main__":
    main()

