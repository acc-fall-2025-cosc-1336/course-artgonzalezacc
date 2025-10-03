import unittest


from src.examples.a_example.devprocess import echo_value, add_numbers, get_tax_amount, TAX_RATE

class Test_Config(unittest.TestCase):

    def test_echo_value(self):
        self.assertEqual("Hello, world!", echo_value("Hello, world!"))
        self.assertEqual(5, echo_value(5))

    def test_add_numbers(self):
        self.assertEqual(5, add_numbers(2, 3))
        self.assertEqual(-1, add_numbers(2, -3))
        self.assertEqual(0, add_numbers(0, 0)) # This will fail

    def test_get_tax_amount(self):
        subtotal = 100
        expected_tax = subtotal * TAX_RATE
        self.assertAlmostEqual(expected_tax, get_tax_amount(subtotal), places=2)

print("Tax rate is:", TAX_RATE)

    
                
