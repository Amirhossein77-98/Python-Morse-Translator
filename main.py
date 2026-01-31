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

def is_morse_valid(morse_code):
    for char in morse_code:
        if char not in ['.', '-', ' ', '/']:
            return False
    return True

def text_to_morse(taxt):
    pass

def morse_to_text(morse_code):
    pass

def main():
    while True:
        print(f"{'*'*5} Morse Code Translator {'*'*5}")
        print("Please choose what you want to do (enter the option number only): ")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Quit")
        
        user_choice: int
        while True:
            try:
                user_choice = int(input("Your choice: "))
                if user_choice in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number (1 or 2).")
                continue
        
        if user_choice == 3:
            print("Exiting the program. Goodbye!")
            break

        while True:
            user_input: str = input(f"Enter your {"Text" if user_choice == 1 else "Morse Code"}: ")
            if user_choice == 1:
                print(f"Original Text: {user_input}")
                print(f"Translated Morse: {text_to_morse(user_input)}")
                break
            elif user_choice == 2 and is_morse_valid(user_input):
                print(f"Original Morse Code: {user_input}")
                print(f"Translated Text: {morse_to_text(user_input)}")
                break
            else:
                print("Invalid Morse Code input. Please try again.")
                continue

if __name__ == "__main__":
    main()