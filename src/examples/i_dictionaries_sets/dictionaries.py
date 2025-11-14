def test_config():
    return True

def create_dictionary():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
    print(phonebook)

def loop_dictionary_w_for():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

    for key in phonebook:
        print(key, phonebook[key])

def loop_dictionary_w_for_items():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

    for key, value in phonebook.items():
        print(key, value)

def loop_dictionary_w_values():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

    for value in phonebook.values():
        print(value)