#main program
from strings import is_substring_in_string

def main():
    choice = 'y'

    while choice.lower() == 'y':
        str = input("Enter a string: ")
        substr = input("Enter a substring to search: ")

        if is_substring_in_string(str, substr):
            print(f'"{substr}" is found in "{str}"')
        else:
            print(f'"{substr}" is NOT found in "{str}"')

        choice = input("Do you want to continue? (y/n): ")

   
if __name__ == "__main__":
    main()