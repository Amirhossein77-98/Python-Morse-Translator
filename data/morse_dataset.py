from dataclasses import dataclass

@dataclass
class MorseCodeDataset:
    """
    A dataset class for Morse code translation.
    This class provides a comprehensive mapping between ASCII characters (letters,
    numbers, and punctuation) and their corresponding Morse code representations.
    Attributes:
        morse_dict (dict): A dictionary mapping characters to Morse code strings.
            - Keys: Single characters including uppercase letters (A-Z), digits (0-9),
                    and various punctuation marks and special characters.
            - Values: Morse code representations using dots (.) and dashes (-),
                     with "/" representing spaces between words.
    Example:
        >>> dataset = MorseCodeDataset()
        >>> dataset.morse_dict["A"]
        '.-'
        >>> dataset.morse_dict["0"]
        '-----'
        >>> dataset.morse_dict[" "]
        '/'
    """

    morse_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": '.----',
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".----.",
        "!": "-.-.--",
        "/": "-..-.",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...",
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "-": "-....-",
        "_": "..--.-",
        '"': ".-..-.",
        "$": "...-..-",
        "@": ".--.-."
    }