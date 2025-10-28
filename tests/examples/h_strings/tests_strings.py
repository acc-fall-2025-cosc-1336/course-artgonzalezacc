import unittest

from src.examples.h_strings.strings import test_config, get_x_char_cnt_of_string, string_concatenation, is_substring_in_string, \
    is_substring_not_in_string, is_file_allowed

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_x_char_cnt_of_string(self):
        self.assertEqual(2, get_x_char_cnt_of_string("C++ is C++ and not Java", "C"))
        self.assertEqual(0, get_x_char_cnt_of_string("C++ is C++ and not Java", "X"))
        self.assertEqual(1, get_x_char_cnt_of_string("C++ is C++ and not Java", "J"))
        self.assertEqual(4, get_x_char_cnt_of_string("C++ is C++ and not Java", "+"))

    def test_string_concatenation(self):
        self.assertEqual("Hello World", string_concatenation("Hello ", "World"))
        self.assertEqual("12345", string_concatenation("12", "345"))
        self.assertEqual("!@#$%", string_concatenation("!@#", "$%"))
        self.assertEqual("Python3.8", string_concatenation("Python", "3.8"))

    def test_is_substring_in_string(self):
        self.assertTrue(is_substring_in_string("Hello World", "World"))
        self.assertFalse(is_substring_in_string("Hello World", "world")) #case sensitive
        self.assertTrue(is_substring_in_string("C++ is C++ and not Java", "C++"))
        self.assertFalse(is_substring_in_string("C++ is C++ and not Java", "JavaScript"))
        self.assertTrue(is_substring_in_string("Python3.8", "3.8"))
        self.assertFalse(is_substring_in_string("Python3.8", "3.9"))

    def test_is_substring_not_in_string(self):
        self.assertFalse(is_substring_not_in_string("Hello World", "World"))
        self.assertTrue(is_substring_not_in_string("Hello World", "world")) #case sensitive
        self.assertFalse(is_substring_not_in_string("C++ is C++ and not Java", "C++"))
        self.assertTrue(is_substring_not_in_string("C++ is C++ and not Java", "JavaScript"))
        self.assertFalse(is_substring_not_in_string("Python3.8", "3.8"))
        self.assertTrue(is_substring_not_in_string("Python3.8", "3.9"))

    def test_string_is_digit(self):
        self.assertTrue("12345".isdigit())
        self.assertFalse("123a45".isdigit())
        self.assertFalse("12 345".isdigit())
        self.assertFalse("".isdigit()) #empty string

    def test_string_is_alpha(self):
        self.assertTrue("HelloWorld".isalpha())
        self.assertFalse("Hello World".isalpha()) #space is not alpha
        self.assertFalse("Hello123".isalpha()) #numbers are not alpha
        self.assertFalse("".isalpha()) #empty string

    def test_string_is_lower_case(self):
        self.assertTrue("helloworld".islower())
        self.assertFalse("HelloWorld".islower())
        self.assertTrue("helloworld123".islower()) #numbers are not lower case
        self.assertFalse("".islower()) #empty string

    def test_convert_string_to_upper_case(self):
        str = "helloworld"

        self.assertEqual("HELLOWORLD", str.upper())
        self.assertEqual(str, "helloworld") #the original string is not affected

        str = "Hello World"
        
        self.assertEqual("HELLO WORLD", str.upper())
        self.assertEqual("12345", "12345".upper()) #numbers are not affected
        self.assertEqual("", "".upper()) #empty string

    def test_strip_string(self):
        str = "   Hello World   "
        self.assertEqual("Hello World", str.strip())

        str = "!!!Hello World!!!"
        self.assertEqual("Hello World", str.strip("!"))

        str = "   !!!Hello World!!!   "
        self.assertEqual("Hello World", str.strip(" !"))

        str = "Hello World"
        self.assertEqual("Hello World", str.strip()) #no leading or trailing spaces

        str = "     "
        self.assertEqual("", str.strip()) #only spaces

        str = ""
        self.assertEqual("", str.strip()) #empty string

    def test_is_file_allowed(self):
        self.assertTrue(is_file_allowed("image.jpg"))
        self.assertTrue(is_file_allowed("photo.jpeg"))
        self.assertTrue(is_file_allowed("graphic.png"))
        self.assertTrue(is_file_allowed("animation.gif"))
        self.assertFalse(is_file_allowed("document.pdf"))
        self.assertFalse(is_file_allowed("archive.zip"))
        self.assertFalse(is_file_allowed("script.py"))
        self.assertFalse(is_file_allowed("image.JPG")) #case sensitive
        self.assertFalse(is_file_allowed("image")) #no extension

    def test_string_repeating_operator(self):
        self.assertEqual("HelloHelloHello", "Hello" * 3)
        self.assertEqual("123123", "123" * 2)
        self.assertEqual("!@#!@#!@#!@#", "!@#" * 4)
        self.assertEqual("", "Hello" * 0) #repeated 0 times
        self.assertEqual("", "" * 5) #empty string repeated any number of times is still empty

    def test_string_replace(self):
        str = "Hello World"
        self.assertEqual("Hello Universe", str.replace("World", "Universe"))
        self.assertEqual("Hello World", str.replace("world", "Universe")) #case sensitive
        self.assertEqual("C++ is C++ and not Python", "C++ is C++ and not Java".replace("Java", "Python"))
        self.assertEqual("C++ is C++ and not Java", "C++ is C++ and not Java".replace("java", "Python")) #case sensitive
        self.assertEqual("aaaaaa", "ababab".replace("b", "a"))
        self.assertEqual("ababab", "ababab".replace("c", "a")) #substring not found, original string returned