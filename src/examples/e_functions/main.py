#main program
from void_functions import display_num

def main():
    num = 10
    print(id(num))
    display_num(num)
    print(num)

main()