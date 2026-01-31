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
        self.morse_dict = MorseCodeDataset.morse_dict

    def is_morse_valid(self, morse_code) -> bool:
        for char in morse_code:
            if char not in ['.', '-', ' ', '/']:
                return False
        return True

    def string_tokenizer(self, string, delimiter) -> list[str]:
        tokens: list[str] = []
        for token in string.split(delimiter):
            tokens.append(token)
        return tokens

    def text_to_morse(self, text) -> str:
        tokens: list[str] = self.string_tokenizer(text.upper(), ' ')
        translated_tokens: list[str] = []
        for token in tokens:
            translated_chars: list[str] = []
            for char in token:
                equivalent_morse_code = self.morse_dict[char]
                translated_chars.append(equivalent_morse_code)
            translated_tokens.append(" ".join(translated_chars))
        return " / ".join(translated_tokens)
    
    def morse_to_text(self, morse_code) -> str:
        tokens: list[str] = self.string_tokenizer(morse_code, ' / ')
        translated_tokens: list[str] = []
        for token in tokens:
            translated_chars: list[str] = []
            for char in token.split(" "):
                char_translation = ""
                for key, value in self.morse_dict.items():
                    if value == char:
                        char_translation = key
                        break
                else:
                    char_translation = "?"
                translated_chars.append(char_translation)
            translated_tokens.append("".join(translated_chars))
        return " ".join(translated_tokens)