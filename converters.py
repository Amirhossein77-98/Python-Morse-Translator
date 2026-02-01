from morse_dataset import MorseCodeDataset

class Converters:
    """
    A utility class for converting between text and Morse code.
    This class provides methods to translate text to Morse code and vice versa,
    along with utility methods for validation and tokenization.
    Attributes:
        morse_dict (dict): A dictionary mapping characters to their Morse code equivalents.
    """
    def __init__(self):
        self.ascii_to_morse_dict: dict[str: str] = MorseCodeDataset.morse_dict
        self.morse_to_ascii_dict: dict[str: str] = {v: k for k, v in MorseCodeDataset.morse_dict.items()}

    def is_morse_valid(self, morse_code: str) -> bool:
        if len(morse_code) == 0: return False
        for char in morse_code:
            if char not in ['.', '-', ' ', '/']:
                return False
        for token in morse_code.split(' '):
            if len(token) > 7:
                return False
            if token.startswith('/') and len(token) > 1:
                return False
        return True

    def string_tokenizer(self, string: str, delimiter: str) -> list[str]:
        return string.split(delimiter)

    def text_to_morse(self, text: str) -> str:
        tokens: list[str] = self.string_tokenizer(text.upper(), ' ')
        translated_tokens: list[str] = []
        for token in tokens:
            translated_chars: list[str] = []
            for char in token:
                try:
                    equivalent_morse_code: str = self.ascii_to_morse_dict[char]
                except:
                    equivalent_morse_code: str = "?"
                translated_chars.append(equivalent_morse_code)
            translated_tokens.append(" ".join(translated_chars))
        return " / ".join(translated_tokens)
    
    def morse_to_text(self, morse_code: str) -> str:
        tokens: list[str] = self.string_tokenizer(morse_code, ' / ')
        translated_tokens: list[str] = []
        for token in tokens:
            translated_chars: list[str] = []
            for char in token.split(" "):
                try:
                    equivalent_ascii_char: str = self.morse_to_ascii_dict[char]
                except:
                    equivalent_ascii_char: str = "?"
                translated_chars.append(equivalent_ascii_char)
            translated_tokens.append("".join(translated_chars))
        return " ".join(translated_tokens)