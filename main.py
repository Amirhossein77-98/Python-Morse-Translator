from converters import Converters
import argparse
from messages import ErrorMessages, MenuMessages, OutputMessages

def main():
    """
    Main entry point for the Morse Code Translator application.
    Provides an interactive command-line interface that allows users to:
    - Convert text to Morse code
    - Convert Morse code back to text
    - Exit the application
    The function runs in a continuous loop until the user chooses to quit.
    For Morse code input, users should use ' / ' as a word separator and 
    single spaces (' ') to separate individual characters.
    Raises:
        ValueError: Handled internally for invalid numeric input during menu selection.
    """

    converter = Converters()
    parser = argparse.ArgumentParser(description="An argument parser to use the code as cli script.")
    parser.add_argument('-m', '--morse', help="To enter morse directly and translate.")
    parser.add_argument('-t', '--text', help="To enter text directly and translate.")
    parser.add_argument('-vm', '--validate_morse', help="To check if a morse code is valid.")
    args = parser.parse_args()
    
    print(f"\n{'*'*5} Morse Code Translator {'*'*5} \n")
    if args.validate_morse:
        if args.morse or args.text:
            print(ErrorMessages.invalid_input_get_cli_help)
        else:
            print(OutputMessages.valid_morse if converter.is_morse_valid(args.validate_morse) else OutputMessages.invalid_morse)
    if args.morse and args.text:
        print(ErrorMessages.invalid_input_get_cli_help)
    if args.morse or args.text:
        if args.morse and converter.is_morse_valid(args.morse):
            print(OutputMessages.original_morse + args.morse)
            print(OutputMessages.translated_text + converter.morse_to_text(args.morse).title() + "\n")
        elif args.text:
            print(OutputMessages.original_text + args.text)
            print(OutputMessages.translated_morse + converter.text_to_morse(args.text) + "\n")
        else:
            print(ErrorMessages.invalid_input)
    else:
        while True:
            print(MenuMessages.menu_prompt)
            print(MenuMessages.menu_options)
            
            user_choice: int
            while True:
                try:
                    user_choice = int(input(MenuMessages.user_choice_input_msg))
                    if user_choice in [1, 2, 3, 4]:
                        break
                    else:
                        print(ErrorMessages.invalid_menu_option_choice)
                except ValueError:
                    print(ErrorMessages.invalid_menu_option_choice)
                    continue
            
            if user_choice == 4:
                print(MenuMessages.exiting_program_msg)
                break

            while True:
                print(MenuMessages.morse_caution) if user_choice == 2 else ""
                user_input: str = input(f"\n> Enter your {"Text" if user_choice == 1 else "Morse Code"}: ").strip()
                if user_choice == 1:
                    print("\n" + OutputMessages.original_text + user_input)
                    print(OutputMessages.translated_morse + converter.text_to_morse(text=user_input))
                    print(f"\n{'='*35}\n")
                    break
                elif user_choice == 2 and converter.is_morse_valid(user_input):
                    print("\n" + OutputMessages.original_morse + user_input)
                    print(OutputMessages.translated_text + converter.morse_to_text(morse_code=user_input).title())
                    print(f"\n{'='*35}\n")
                    break
                elif user_choice == 3:
                    print(OutputMessages.valid_morse if converter.is_morse_valid(user_input) else OutputMessages.invalid_morse)
                else:
                    print(ErrorMessages.invalid_morse_input)
                    continue

if __name__ == "__main__":
    main()