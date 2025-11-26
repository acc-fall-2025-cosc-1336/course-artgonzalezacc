class BankAccount:

    __balance = 0 #private variable (only modifiable within the scope of BankAccount)

    def get_balance(self):
        return self.__balance
        