import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_bank_account_get_balance(self):
        account = BankAccount() #create a variable of type BankAccount / object of BankAccount
        
        self.assertEqual(0, account.get_balance())