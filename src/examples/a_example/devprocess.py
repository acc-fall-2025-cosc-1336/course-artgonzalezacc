TAX_RATE = .07 #NAMED CONSTANT
print("Tax rate is:", TAX_RATE)
def hello_world(name):
     print("Hello, " + name + "!")

def echo_value(value):
    return value

def add_numbers(num1, num2):
    return num1 + num2

def get_tax_amount(subtotal):
    TAX_RATE = .09
    return subtotal * TAX_RATE