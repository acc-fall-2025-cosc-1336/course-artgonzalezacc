import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_access_dictionary_value(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        expected_value = 'Katie'

        value = phonebook['555-2222']

        self.assertEqual(value, expected_value)

    def test_exception_when_key_not_in_dictionary(self):

        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        
        with self.assertRaises(KeyError):
            phonebook['555-1110']

    def test_key_in_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        key = '555-3333'

        self.assertEqual(True, key in phonebook)

    def test_key_not_in_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        key = '555-0000'

        self.assertEqual(True, key not in phonebook)

    def test_add_pair_to_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        phonebook['555-4444'] = 'Chris'
        expected_value = 'Chris'

        self.assertEqual(phonebook['555-4444'], expected_value)

    def test_update_dictionary_value(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

        phonebook['555-1111'] = 'Cris'

        self.assertEqual(phonebook['555-1111'], 'Cris')

    def test_delete_key_value_pair(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        del phonebook['555-2222']

        self.assertEqual(True, '555-2222' not in phonebook)

    def test_count_dictionary_key_value_pairs(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        expected_count = 3

        self.assertEqual(True, expected_count == len(phonebook))

    def test_dictionary_values_as_list(self):
        test_scores = {'Kayla':[88, 92, 100], 'Luis':[95, 74, 84], 'Sophie':[72, 88, 91], 'Ethan':[70, 75, 78]}

        expected_value = [72, 88, 91]

        self.assertEqual(expected_value, test_scores['Sophie'])

    def test_dictionary_values_dif_data_types(self):
        mixed_up = {'abc':1, 999:'yada yada', (3, 6, 9):[3, 6, 9]}

        expected_value = [3, 6, 9]

        self.assertEqual(mixed_up[(3,6,9)], expected_value)

    def test_create_empty_dictionary_add_values(self):
        phonebook = {} # phonebook = dict()
        phonebook['555-1111'] = 'Chris'
        phonebook['555-2222'] = 'Katie'
        phonebook['555-3333'] = 'Joanne'

        self.assertEqual('Chris', phonebook['555-1111'])

    def test_clear_dictionary(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

        phonebook.clear()

        self.assertEqual(phonebook, {})

    def test_dictionary_pop_key_value_pair(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        expected_value = 'Chris'

        popped_value = phonebook.pop('555-1111', 'Does not exist')

        self.assertEqual(popped_value, expected_value)
        self.assertEqual(True, '555-1111' not in phonebook)

    def test_dictionary_pop_key_value_pair_not_exist(self):
        phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
        expected_value = 'Does not exist'

        popped_value = phonebook.pop('555-1112', 'Does not exist')

        self.assertEqual(popped_value, expected_value)




