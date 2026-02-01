from morse_dataset import MorseCodeDataset

class HelperFunctions:
    """
    A collection of static helper functions for Morse code translation.
    Methods
    -------
    is_morse_valid(morse_code: str) -> bool
        Checks if the given Morse code string is valid.
        A valid Morse code string contains only '.', '-', ' ', and '/' characters.
        Additionally, each token (separated by spaces) must not exceed 6 characters,
        and tokens starting with '/' must not have additional characters.
    string_tokenizer(string: str, delimiter: str) -> list[str]
        Splits the input string into a list of substrings using the specified delimiter.
    """

    @staticmethod
    def is_morse_valid(morse_code: str) -> bool:
        if len(morse_code) == 0: return False
        for char in morse_code:
            if char not in ['.', '-', ' ', '/']:
                return False
        for token in morse_code.split(' '):
            if len(token) > 6 or (token.startswith('/') and len(token) > 1):
                return False
        return True
    
    @staticmethod
    def string_tokenizer(string: str, delimiter: str) -> list[str]:
        return string.split(delimiter)


class Converters:
    """
    A class for converting between ASCII text and Morse code.
    This class provides bidirectional conversion capabilities between standard ASCII
    text and Morse code representation. It uses a Morse code dataset to maintain
    mappings in both directions (ASCII to Morse and Morse to ASCII).
    Attributes:
        ascii_to_morse_dict (dict[str, str]): Dictionary mapping ASCII characters to their Morse code equivalents.
        morse_to_ascii_dict (dict[str, str]): Dictionary mapping Morse code sequences to their ASCII character equivalents.
    Methods:
        text_to_morse(text: str) -> str:
            Converts ASCII text to Morse code representation.
        morse_to_text(morse_code: str) -> str:
            Converts Morse code representation to ASCII text.
    """

    def __init__(self):
        self.ascii_to_morse_dict: dict[str, str] = MorseCodeDataset.morse_dict
        self.morse_to_ascii_dict: dict[str, str] = {v: k for k, v in MorseCodeDataset.morse_dict.items()}

    def text_to_morse(self, text: str) -> str:
        tokens: list[str] = HelperFunctions.string_tokenizer(text.upper(), ' ')
        translated_tokens: list[str] = []
        for token in tokens:
            translated_chars: list[str] = []
            for char in token:
                try:
                    equivalent_morse_code: str = self.ascii_to_morse_dict[char]
                except KeyError:
                    equivalent_morse_code: str = "?"
                translated_chars.append(equivalent_morse_code)
            translated_tokens.append(" ".join(translated_chars))
        return " / ".join(translated_tokens)
    
    def morse_to_text(self, morse_code: str) -> str:
        tokens: list[str] = HelperFunctions.string_tokenizer(morse_code, ' / ')
        translated_tokens: list[str] = []
        for token in tokens:
            translated_chars: list[str] = []
            for char in token.split(" "):
                try:
                    equivalent_ascii_char: str = self.morse_to_ascii_dict[char]
                except KeyError:
                    equivalent_ascii_char: str = "?"
                translated_chars.append(equivalent_ascii_char)
            translated_tokens.append("".join(translated_chars))
        return " ".join(translated_tokens)