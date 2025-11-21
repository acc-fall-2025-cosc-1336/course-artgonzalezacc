#
def write_to_file(file_name):

    file = open(file_name, 'w')

    file.write('John Locke\n')
    file.write('David Hume\n')
    file.write('Edmund Burke\n')

    file.close()

def read_from_file(file_name):
    
    file = open(file_name, 'r')

    file_lines = file.read()
    file.close()

    print(file_lines)

def read_from_file_one_line_at_a_time(file_name):
    
    file = open(file_name, 'r')

    line1 = file.readline().rstrip('\n')
    line2 = file.readline().rstrip('\n')
    line3 = file.readline().rstrip('\n')

    file.close()

    print(line1)
    print(line2)
    print(line3)

def read_from_file_w_while_loop(file_name):

    file = open(file_name, 'r')

    line = file.readline().rstrip('\n')

    while line != '':
        print(line)
        line = file.readline().rstrip('\n')

    file.close()

def write_employee_records(file_name):

    file = open(file_name, 'w')

    choice = '1'

    while choice == '1':

        id = input('Enter id: ')
        name = input('Enter name: ')
        dept = input('Enter dept: ')

        file.write(id + '\t')
        file.write(name + '\t')
        file.write(dept + '\n')

        choice = input('Enter 1 to continue...')

def read_employee_records(file_name):

    file = open(file_name, 'r')

    for employee in file:
        record = employee.split('\t') #creates a list ['1', 'C++', 'Programming]
        id = record[0]
        name = record[1]
        dept = record[2]

        print(id, name, dept)

    file.close()

prog_langs = [['1980', 'C++', 'Complex'], ['1996', 'Python', 'Easy'], ['1991', 'Java', 'Medium']]

def write_list_of_lists(file_name):

    file = open(file_name, 'w')

    for lang in prog_langs:
        file.write(lang[0] + '\t')
        file.write(lang[1] + '\t')
        file.write(lang[2] + '\n')

    file.close()

def read_lists_of_lists_from_file(file_name):
    
    file = open(file_name, 'r')

    list_langs = []

    for line in file:
        record = line.split('\t') #creates a list
        
        record[2] = record[2].rstrip('\n')
        
        list_langs.append(record)

    file.close()
    
    print(list_langs)

prog_langs = {'1' : ['1979', 'C++', 'Bjarne'], '2': ['1991', 'Java', 'Gosling'], '3': ['1996', 'Python', 'Guido']}

def write_dictionary_records(file_name):
    
    with open(file_name, 'w') as file:
        for key, list_record in prog_langs.items():
            file.write(key + '\t')
            file.write(list_record[0] + '\t')
            file.write(list_record[1] + '\t')
            file.write(list_record[2] + '\n')

def read_dictionary_records(file_name):

    prog_langs = {}

    with open(file_name, 'r') as file:
        for line in file:
            record =  line.split('\t')
            record[2] = record[2].rstrip('\n')

            key = record[0]
            year = record[1]
            lang = record[2]
            creator = record[3].rstrip('\n')

            prog_langs[key] = [year, lang, creator]

    print(prog_langs)



