import unittest
from core.converters import Converters

class ConvertersTest(unittest.TestCase):
    """
    Unit tests for the Converters class.
    This test suite validates the functionality of text-to-morse and morse-to-text
    conversion operations. It covers:
    - Alphabetic characters (A-Z)
    - Numeric characters (0-9)
    - Punctuation marks (!@.,'!/()&:;=+-_"$)
    - Single words
    - Complete sentences with spaces and punctuation
    The tests ensure bidirectional conversion accuracy and proper handling of
    special characters, spaces, and mixed-case inputs.
    """

    def setUp(self):
        self.converter = Converters()

    # Text to Morse Test Units
    def test_text_to_morse_alphabets(self):
        self.assertEqual(self.converter.text_to_morse("ABCDEFG"), ".- -... -.-. -.. . ..-. --.")
        self.assertEqual(self.converter.text_to_morse("HIJKLMN"), ".... .. .--- -.- .-.. -- -.")
        self.assertEqual(self.converter.text_to_morse("OPQRSTU"), "--- .--. --.- .-. ... - ..-")
        self.assertEqual(self.converter.text_to_morse("VWXYZ"), "...- .-- -..- -.-- --..")

    def test_text_to_morse_numbers(self):
        self.assertEqual(self.converter.text_to_morse("0123"), "----- .---- ..--- ...--")
        self.assertEqual(self.converter.text_to_morse("456"), "....- ..... -....")
        self.assertEqual(self.converter.text_to_morse("789"), "--... ---.. ----.")

    def test_text_to_morse_punctuations(self):
        self.assertEqual(self.converter.text_to_morse("!@."), "-.-.-- .--.-. .-.-.-")
        self.assertEqual(self.converter.text_to_morse(" ,?"), "--..-- ..--..")
        self.assertEqual(self.converter.text_to_morse("'!/"), ".----. -.-.-- -..-.")
        self.assertEqual(self.converter.text_to_morse("()&"), "-.--. -.--.- .-...")
        self.assertEqual(self.converter.text_to_morse(":;="), "---... -.-.-. -...-")
        self.assertEqual(self.converter.text_to_morse("+-_"), ".-.-. -....- ..--.-")
        self.assertEqual(self.converter.text_to_morse('"$_'), ".-..-. ...-..- ..--.-")

    def test_text_to_morse_words(self):
        self.assertEqual(self.converter.text_to_morse("Hello"), ".... . .-.. .-.. ---")
        self.assertEqual(self.converter.text_to_morse("Quantum"), "--.- ..- .- -. - ..- --")
        self.assertEqual(self.converter.text_to_morse("What"), ".-- .... .- -")
        self.assertEqual(self.converter.text_to_morse("Live"), ".-.. .. ...- .")
        self.assertEqual(self.converter.text_to_morse("Migration"), "-- .. --. .-. .- - .. --- -.")

    def test_text_to_morse_sentences(self):
        self.assertEqual(self.converter.text_to_morse("Hello World"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
        self.assertEqual(self.converter.text_to_morse("That's OK."), "- .... .- - .----. ... / --- -.- .-.-.-")
        self.assertEqual(self.converter.text_to_morse("How are you?"), ".... --- .-- / .- .-. . / -.-- --- ..- ..--..")
        self.assertEqual(self.converter.text_to_morse("Quantum Physics!"), "--.- ..- .- -. - ..- -- / .--. .... -.-- ... .. -.-. ... -.-.--")
        self.assertEqual(self.converter.text_to_morse("I want to be free "), ".. / .-- .- -. - / - --- / -... . / ..-. .-. . .")

    # Morse to Text Test Units
    def test_morse_to_text_alphabets(self):
        self.assertEqual(self.converter.morse_to_text(".- -... -.-. -.. . ..-. --."), "ABCDEFG")
        self.assertEqual(self.converter.morse_to_text(".... .. .--- -.- .-.. -- -."), "HIJKLMN" )
        self.assertEqual(self.converter.morse_to_text("--- .--. --.- .-. ... - ..-"), "OPQRSTU")
        self.assertEqual(self.converter.morse_to_text("...- .-- -..- -.-- --.."), "VWXYZ")

    def test_morse_to_text_numbers(self):
        self.assertEqual(self.converter.morse_to_text("----- .---- ..--- ...--"), "0123" )
        self.assertEqual(self.converter.morse_to_text("....- ..... -...."), "456")
        self.assertEqual(self.converter.morse_to_text("--... ---.. ----."), "789")

    def test_morse_to_text_punctuations(self):
        self.assertEqual(self.converter.morse_to_text("-.-.-- .--.-. .-.-.-"), "!@.")
        self.assertEqual(self.converter.morse_to_text(" / --..-- ..--.."), " ,?")
        self.assertEqual(self.converter.morse_to_text(".----. -.-.-- -..-."), "'!/")
        self.assertEqual(self.converter.morse_to_text("-.--. -.--.- .-..."), "()&")
        self.assertEqual(self.converter.morse_to_text("---... -.-.-. -...-"), ":;=")
        self.assertEqual(self.converter.morse_to_text(".-.-. -....- ..--.-"), "+-_")
        self.assertEqual(self.converter.morse_to_text(".-..-. ...-..- ..--.-"), '"$_')

    def test_morse_to_text_words(self):
        self.assertEqual(self.converter.morse_to_text(".... . .-.. .-.. ---").lower(), "Hello".lower())
        self.assertEqual(self.converter.morse_to_text("--.- ..- .- -. - ..- --").lower(), "Quantum".lower())
        self.assertEqual(self.converter.morse_to_text(".-- .... .- -").lower(), "What".lower())
        self.assertEqual(self.converter.morse_to_text(".-.. .. ...- .").lower(), "Live".lower())
        self.assertEqual(self.converter.morse_to_text("-- .. --. .-. .- - .. --- -.").lower(), "Migration".lower())

    def test_morse_to_text_sentences(self):
        self.assertEqual(self.converter.morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -..").lower(), "Hello World".lower())
        self.assertEqual(self.converter.morse_to_text("- .... .- - .----. ... / --- -.- .-.-.-").lower(), "That's OK.".lower())
        self.assertEqual(self.converter.morse_to_text(".... --- .-- / .- .-. . / -.-- --- ..- ..--..").lower(), "How are you?".lower())
        self.assertEqual(self.converter.morse_to_text("--.- ..- .- -. - ..- -- / .--. .... -.-- ... .. -.-. ... -.-.--").lower(), "Quantum Physics!".lower())
        self.assertEqual(self.converter.morse_to_text(".. / .-- .- -. - / - --- / -... . / ..-. .-. . . / ").lower(), "I want to be free ".lower())
