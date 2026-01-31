from converters import Converters

def main():
    converter = Converters()
    print(f"\n{'*'*5} Morse Code Translator {'*'*5} \n")
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
                    print("Invalid choice. Please enter 1, 2 or 3.")
            except ValueError:
                print("Invalid input. Please enter a number (1, 2 or 3).")
                continue
        
        if user_choice == 3:
            print("\n##### Exiting the program. Goodbye!\n")
            break

        while True:
            print("\n!!!CAUTION: Please use ' / ' as 'space' or seperator between words and simple space (' ') to separate characters.") if user_choice == 2 else ""
            user_input: str = input(f"\n> Enter your {"Text" if user_choice == 1 else "Morse Code"}: ").strip()
            if user_choice == 1:
                print(f"\n>>> Original Text: {user_input}")
                print(f">>> Translated Morse: {converter.text_to_morse(text=user_input)}")
                print(f"\n{'='*35}\n")
                break
            elif user_choice == 2 and converter.is_morse_valid(user_input):
                print(f"\n>>> Original Morse Code: {user_input}")
                print(f">>> Translated Text: {converter.morse_to_text(morse_code=user_input).title()}")
                print(f"\n{'='*35}\n")
                break
            else:
                print("Invalid Morse Code input. Please try again.")
                continue

if __name__ == "__main__":
    main()