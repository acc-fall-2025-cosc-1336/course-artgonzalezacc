#
state_sales_tax_rate = .085

def say_hello():
    print(state_sales_tax_rate)

def display_num(num):
    print(state_sales_tax_rate)

def print_global_variable():
    state_sales_tax_rate = 1 #created a function/local variable IT'S NOT USING THE GLOBAL VARIABLE
    print(state_sales_tax_rate)

def change_global_variable_value():
    global state_sales_tax_rate #use global variable
    state_sales_tax_rate = .09 #overwrite the global variable
    
    print(state_sales_tax_rate)

def variable_in_if_block():
    if(True):
        num = 20
        print(num)

    print(num)

def variable_in_while_block():
    cnt = 3

    while(cnt > 0):
        num = 20
        cnt -= 1

    print(num)
