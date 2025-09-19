from decisions import compare_strings

def main():
    str1 = input('Enter first string: ')
    str2 = input('Enter second string: ')

    result = compare_strings(str1, str2)

    if(result):
        print('The strings are equal')
    else:
        print('The strings are not equal')

if __name__ == "__main__":
    main()
