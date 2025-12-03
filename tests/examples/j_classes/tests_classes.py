import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_bank_account_get_balance(self):
        account = BankAccount(500) #create a variable of type BankAccount / object of BankAccount
        
        self.assertEqual(500, account.get_balance())

    def test_deposit_w_positive_value(self):
        account = BankAccount(500)

        account.deposit(100)

        self.assertEqual(600, account.get_balance())

    def test_deposit_w_negative_balance(self):

        account = BankAccount(500)

        account.deposit(-100)

        self.assertEqual(500, account.get_balance())

    def test_deposit_w_two_bank_account_variables(self):
        account1 = BankAccount(500)
        account2 = BankAccount(600)

        self.assertEqual(500, account1.get_balance())
        self.assertEqual(600, account2.get_balance())

        account1.deposit(500)
        self.assertEqual(1000, account1.get_balance())

        account2.deposit(600)
        self.assertEqual(1200, account2.get_balance())