from bank_account import BankAccount
from atm import ATM

def main():
    account = BankAccount(1000) #create a variable of type balance
    print("balance: ", account.get_balance() ) #get the balance with get_balance

    atm = ATM(account)

    atm.display_balance()

    atm.make_deposit()

    atm.display_balance()

    atm.make_withdraw()

    atm.display_balance()

    account = BankAccount(500)

    atm = ATM(account)

    atm.display_balance()
    

main()