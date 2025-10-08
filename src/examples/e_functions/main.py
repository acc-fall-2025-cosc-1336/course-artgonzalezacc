#main program
from value_return_functions import get_head_or_tail

def main():
    choice = 'Y'

    while(choice == 'y' or choice == 'Y'):
        
        result = get_head_or_tail()
        
        if result == 1:
            print("It's Heads")
        else:
            print("It's Tails")

        choice = input("Do you want to flip again? (Y/N): ")

main()