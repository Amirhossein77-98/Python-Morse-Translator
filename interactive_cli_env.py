from messages import MenuMessages, UIElements, ErrorMessages, OutputMessages
from converters import Converters, HelperFunctions

class InteractiveCLIEnvironment:
    """
    A class that manages the interactive command-line interface for a Morse code translator application.
    This class handles user interaction, menu navigation, and coordinates with a Morse code converter
    to perform translation operations between text and Morse code.
    Attributes:
        converter (Converters): An instance of the Converters class responsible for performing
            text-to-Morse and Morse-to-text conversions, as well as validation.
    Methods:
        show_menu_and_get_user_input() -> int:
            Displays the main menu to the user and retrieves their menu choice.
            Validates that the input is an integer between 1 and 4.
            Returns the user's valid menu choice.
        main_app_body() -> None:
            Executes the main application loop that handles user interactions.
            Continuously displays the menu, processes user selections, and performs
            the corresponding operation (text-to-Morse conversion, Morse-to-text conversion,
            Morse validation, or program exit).
    """

    def __init__(self, converter: Converters):
        self.converter: Converters = converter

    def show_menu_and_get_user_input(self) -> int:
        print(MenuMessages.menu_prompt)
        print(MenuMessages.menu_options)
        
        user_choice: int
        
        while True:
            try:
                user_choice = int(input(MenuMessages.user_choice_input_msg).lstrip())
                if user_choice in [1, 2, 3, 4]:
                    return user_choice
                else:
                    print(ErrorMessages.invalid_menu_option_choice)
                    continue
            except ValueError:
                print(ErrorMessages.invalid_menu_option_choice)
                continue

    def main_app_body(self):
        while True:
            user_choice = self.show_menu_and_get_user_input()
            
            if user_choice == 4:
                print(MenuMessages.exiting_program_msg)
                break

            while True:
                print(MenuMessages.morse_caution) if user_choice == 2 else ""
                
                user_input: str = input(MenuMessages.prompt_for_text if user_choice == 1 else MenuMessages.prompt_for_morse).lstrip()
                
                if user_choice == 1:
                    print("\n" + OutputMessages.original_text + user_input)
                    print(OutputMessages.translated_morse + self.converter.text_to_morse(text=user_input))
                    print(UIElements.separator)
                    break
                elif user_choice == 2 and HelperFunctions.is_morse_valid(user_input):
                    print("\n" + OutputMessages.original_morse + user_input)
                    print(OutputMessages.translated_text + self.converter.morse_to_text(morse_code=user_input).title())
                    print(UIElements.separator)
                    break
                elif user_choice == 3:
                    print(OutputMessages.valid_morse if HelperFunctions.is_morse_valid(user_input) else OutputMessages.invalid_morse)
                else:
                    print(ErrorMessages.invalid_morse_input)
                    continue
