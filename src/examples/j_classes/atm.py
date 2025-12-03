class ATM:
    __account = ''

    def __init__(self, account):
        self.__account = account

    def display_balance(self):
        print(self.__account.get_balance())

    def make_deposit(self):
        amt = int(input("Enter amount to deposit: "))

        self.__account.deposit(amt)

    def make_withdraw(self):
        amt = int(input("Enter amount to withdraw: "))
        self.__account.withdraw(amt)
    

#FREE FUNCTIONS-are not part of the ATM class

def display_menu():
    print('ACC Bank')
    print('1-Display Balance')
    print('2-Make Deposit')
    print('3-Make Withdraw')
    print('4-Exit')

def run_menu(atm):

    choice = '1'

    while(choice != '4'):

        display_menu()
        choice = input('Enter menu choice: ')
        handle_menu_option(atm, choice)


def handle_menu_option(atm, choice):

    if choice == '1':
        atm.display_balance()
    elif choice == '2':
        atm.make_deposit()
    elif choice == '3':
        atm.make_withdraw()
    elif choice == '4':
        print('Exiting..')
    else:
        print('Invalid option.')

    