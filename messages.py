"""
Module containing dataclass definitions for application messages and UI elements.

This module defines several dataclasses that centralize all user-facing strings
used throughout the Morse Code Translator application, including error messages,
menu prompts, output messages, and UI elements.

Classes:
    AppName: Stores the application name.
    ErrorMessages: Contains error message strings for various error conditions.
    MenuMessages: Contains menu-related prompts and options.
    OutputMessages: Contains output message strings for translation results.
    UIElements: Contains UI visual elements and separators.
"""
from dataclasses import dataclass
from textwrap import dedent

@dataclass
class AppName:
    app_name: str = "Morse Code Translator"

@dataclass
class ErrorMessages:
    invalid_input_get_cli_help: str = "Invalid Input. Please use '--help' to find cli args."
    invalid_input: str = "Invalid Input."
    invalid_menu_option_choice: str = "Invalid choice/input. Please enter 1, 2, 3 or 4."
    invalid_morse_input: str = "Invalid Morse Code input. Please try again."

@dataclass
class MenuMessages:
    menu_prompt: str = "Please choose what you want to do (enter the option number only): "
    menu_options: str = dedent("""
    1. Text to Morse Code
    2. Morse Code to Text
    3. Validate Morse Code
    4. Quit
    """)
    user_choice_input_msg: str = "> Your choice: "
    exiting_program_msg: str = "\n##### Exiting the program. Goodbye!\n"
    morse_caution: str = "\n!!!CAUTION: Please use ' / ' as 'space' or seperator between words and simple space (' ') to separate characters."
    prompt_for_text: str = "Enter your Text: "
    prompt_for_morse: str = "Enter your Morse Code: "

@dataclass
class OutputMessages:
    original_text: str = ">>> Original Text: "
    original_morse: str = ">>> Original Morse Code: "
    translated_text: str = ">>> Translated Text: "
    translated_morse: str = ">>> Translated Morse Code: "
    valid_morse: str = ">>> It's Valid Morse.\n"
    invalid_morse: str = ">>> It's NOT a Valid Morse.\n"

@dataclass
class UIElements:
    separator: str = f"\n{'='*35}\n"