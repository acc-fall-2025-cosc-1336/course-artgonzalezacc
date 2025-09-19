from decisions import is_vowel

def main():
    char = input('Enter a letter: ')

    result = is_vowel(char)

    if(result):
        print(char, 'is vowel')
   

if __name__ == "__main__":
    main()
