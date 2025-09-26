def test_config():
    return True

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def is_vowel(char):
    return char == 'a' or char== 'e' or char == 'i' or char == 'o' or char == 'u'

def compare_strings(str1, str2):
    return str1 == str2

def is_number_in_range(num, start, end):
    return num >= start and num <= end

def is_number_not_in_range(num, start, end):
    return num < start or num > end

def get_generation(year):
    generation = ""

    if(year >= 1996 and year <= 2014):
       generation = "Centennial" 
    elif(year >= 1977 and year <= 1995):
        generation = "Milennial"
    elif(year >= 1965 and year <= 1976):
        generation = "Generation X"
    elif(year >= 1946 and year <= 1964):
        generation = "Baby Boomer"
    elif(year >= 1925 and year <= 1945):
        generation = "Silent Generation"
    else:
        generation = "Invalid Year"

    return generation
    
    

