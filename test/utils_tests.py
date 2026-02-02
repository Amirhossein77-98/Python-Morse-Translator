import unittest
from utilities.utils import HelperFunctions

class UtilsTest(unittest.TestCase):
    """
    Unit tests for utility functions in the Morse Translator project.
    Classes:
        UtilsTest(unittest.TestCase): 
            Contains tests for validating Morse code strings and tokenizing strings.
    Methods:
        test_morse_validator:
            Tests the is_morse_valid function to ensure it correctly identifies valid and invalid Morse code strings.
        test_string_tokenizer:
            Tests the string_tokenizer function to verify correct splitting of strings based on a given delimiter.
    """

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
