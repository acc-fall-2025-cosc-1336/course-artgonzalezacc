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


