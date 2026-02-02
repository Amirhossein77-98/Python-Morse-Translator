import unittest
from utilities.utils import HelperFunctions

class UtilsTest(unittest.TestCase):

    def test_morse_validator(self):
        self.assertEqual(HelperFunctions.is_morse_valid(". .. -. ... - . .. -."), True)
        self.assertEqual(HelperFunctions.is_morse_valid("..--- ----- ..--- -...."), True)
        self.assertEqual(HelperFunctions.is_morse_valid(".-.-.- .----. "), True)
        self.assertEqual(HelperFunctions.is_morse_valid("....... . . ."), False)
        self.assertEqual(HelperFunctions.is_morse_valid(". . - - // .--."), False)
        self.assertEqual(HelperFunctions.is_morse_valid(".... . .-.. .-.. o"), False)

    def test_string_tokenizer(self):
        self.assertEqual(HelperFunctions.string_tokenizer("Hello World!", " "), ["Hello", "World!"])
        self.assertEqual(HelperFunctions.string_tokenizer("Yes Ok No Aha", " "), ["Yes", "Ok", "No", "Aha"])
        self.assertEqual(HelperFunctions.string_tokenizer(".. / ...", " / "), ["..", "..."])
        self.assertEqual(HelperFunctions.string_tokenizer(".. ... / .-.- .", " / "), [".. ...", ".-.- ."])
