#
state_sales_tax_rate = .085

def say_hello():
    print('hello')
    print(state_sales_tax_rate)

def display_num(num):
    print(num)
    num = 20
    print(id(num))
    print(state_sales_tax_rate)

def print_global_variable():
    state_sales_tax_rate = 1 #created a function/local variable IT'S NOT USING THE GLOBAL VARIABLE
    print(state_sales_tax_rate)

