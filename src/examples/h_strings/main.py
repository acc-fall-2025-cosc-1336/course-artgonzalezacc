#main program
from strings import is_substring_in_string

def main():
    in_str = is_substring_in_string("Four score and seven years ago", "Seven")

    if(in_str):
        print("The substring was found in the string")
    else:
        print("The substring was NOT found in the string")

   
if __name__ == "__main__":
    main()