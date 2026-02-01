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