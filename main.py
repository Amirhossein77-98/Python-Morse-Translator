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
    "&": ".-..."
}

def is_morse_valid(morse_code) -> bool:
    for char in morse_code:
        if char not in ['.', '-', ' ', '/']:
            return False
    return True

def string_tokenizer(string, delimiter) -> list[str]:
    tokens = []
    for token in string.split(delimiter):
        tokens.append(token)
    return tokens

def text_to_morse(text) -> str:
    tokens: list[str] = string_tokenizer(text.upper(), ' ')
    translated_tokens: list[str] = []
    for token in tokens:
        translated_chars: list[str] = []
        for char in token:
            equivalent_morse_code = morse_dict[char]
            translated_chars.append(equivalent_morse_code)
        translated_tokens.append(" ".join(translated_chars))
    return " / ".join(translated_tokens)

def morse_to_text(morse_code) -> str:
    pass

def main():
    print(f"{'*'*5} Morse Code Translator {'*'*5} \n")
    while True:
        print("Please choose what you want to do (enter the option number only): ")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Quit")
        
        user_choice: int
        while True:
            try:
                user_choice = int(input("> Your choice: "))
                if user_choice in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number (1 or 2).")
                continue
        
        if user_choice == 3:
            print("\n##### Exiting the program. Goodbye!\n")
            break

        while True:
            user_input: str = input(f"\nEnter your {"Text" if user_choice == 1 else "Morse Code"}: ").strip()
            if user_choice == 1:
                print(f"\n>>> Original Text: {user_input}")
                print(f">>> Translated Morse: {text_to_morse(user_input)}")
                print(f"\n{'='*25}\n")
                break
            elif user_choice == 2 and is_morse_valid(user_input):
                print(f"\n>>> Original Morse Code: {user_input}")
                print(f">>> Translated Text: {morse_to_text(user_input)}")
                print(f"\n{'='*25}\n")
                break
            else:
                print("Invalid Morse Code input. Please try again.")
                continue

if __name__ == "__main__":
    main()