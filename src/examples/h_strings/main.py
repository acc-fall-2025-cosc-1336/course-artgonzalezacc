#main program
from strings import get_x_char_cnt_of_string

def main():
    name = "C++ C# Java and Python"
    choice = 'Y'

    while(choice == 'Y' or choice == 'y'):
        char = input("Enter the character to count: ")
        count = get_x_char_cnt_of_string(name, char)
        print(f"The character '{char}' appears {count} times in the string.")
        choice = input("Do you want to continue? (Y/N): ")
        

if __name__ == "__main__":
    main()