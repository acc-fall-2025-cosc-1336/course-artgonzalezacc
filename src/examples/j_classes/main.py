from bank_account import BankAccount

def main():
    account = BankAccount(1000) #create a variable of type balance
    print("balance: ", account.get_balance() ) #get the balance with get_balance

    amt = int(input("Enter amount to deposit: "))

    account.deposit(amt)
    print("balance: ", account.get_balance() ) #get the balance with get_balance

    amt = int(input("Enter amount to withdraw: "))
    account.withdraw(amt)
    print("balance: ", account.get_balance() ) #get the balance with get_balance

main()