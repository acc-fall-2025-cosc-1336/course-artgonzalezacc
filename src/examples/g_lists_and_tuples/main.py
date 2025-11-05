#main program
from lists import generate_lottery_numbers, display_lottery_numbers

def main():
    lottery_list = generate_lottery_numbers(7)
    display_lottery_numbers(lottery_list)

if __name__ == "__main__":
    main()