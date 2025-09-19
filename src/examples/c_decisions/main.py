from decisions import get_generation

def main():
    year = int(input('Enter year: '))
    result = get_generation(year)
    print(f'Generation: {result}')

if __name__ == "__main__":
    main()
