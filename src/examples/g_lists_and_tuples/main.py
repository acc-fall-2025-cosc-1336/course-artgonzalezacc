#main program
from lists import get_multiplication_table, display_multiplication_table

def main():
    table = get_multiplication_table(10,10)
    display_multiplication_table(table)

if __name__ == "__main__":
    main()