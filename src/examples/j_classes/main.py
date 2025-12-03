from bank_account import BankAccount
from atm import ATM, run_menu

def main():
    account = BankAccount(1000) #create a variable of type balance
    
    atm = ATM(account)

    run_menu(atm)


main()