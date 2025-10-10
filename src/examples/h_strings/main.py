#main program
def main():
    name = "C++"
    name[0] = 'c'  # This will raise an error because strings are immutable

if __name__ == "__main__":
    main()