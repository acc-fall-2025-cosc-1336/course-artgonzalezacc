class BankAccount:

    __balance = 0 #private variable (only modifiable within the scope of BankAccount)

    def __init__(self, balance): #class constructor/initialize class member variables
        self.__balance = balance
    
    def get_balance(self): 
        return self.__balance
        