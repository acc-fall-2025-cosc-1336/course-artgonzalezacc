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

    def test_withdraw_w_positive_amount(self):
        account = BankAccount(500)

        account.withdraw(100)

        self.assertEqual(400, account.get_balance())

    def test_withdraw_w_negative_amount(self):
        account = BankAccount(500)

        account.withdraw(-100)

        self.assertEqual(500, account.get_balance())

    def test_withdraw_w_two_objects(self):
        account1 = BankAccount(1000)
        account2 = BankAccount(2000)
        
        self.assertEqual(1000, account1.get_balance())
        self.assertEqual(2000, account2.get_balance())

        account1.withdraw(100)
        self.assertEqual(900, account1.get_balance())

        account2.withdraw(100)
        self.assertEqual(1900, account2.get_balance())