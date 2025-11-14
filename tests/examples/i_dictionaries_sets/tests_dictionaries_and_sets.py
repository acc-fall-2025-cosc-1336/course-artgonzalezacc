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

