import argparse
from views.messages import OutputMessages, ErrorMessages
from core.converters import HelperFunctions
import views.ui

class ArgParser:
    def __init__(self):
        self.parser: argparse.ArgumentParser = argparse.ArgumentParser(description="An argument parser to use the code as cli script.")
        self.parser.add_argument('-m', '--morse', help="To enter morse directly and translate.")
        self.parser.add_argument('-t', '--text', help="To enter text directly and translate.")
        self.parser.add_argument('-vm', '--validate_morse', help="To check if a morse code is valid.")
        self.parser.add_argument('-ui', '--user_interface', action='store_true', help="To launch UI.")   
        self.args: argparse.Namespace
    
    def parse(self) -> argparse.Namespace:
        self.args = self.parser.parse_args()
        return self.args
    
    def do_args_action(self, converter):
        if self.args.morse and HelperFunctions.is_morse_valid(self.args.morse):
            print(OutputMessages.original_morse + self.args.morse.strip())
            print(OutputMessages.translated_text + converter.morse_to_text(self.args.morse.strip()).title() + "\n")
        elif self.args.text:
            print(OutputMessages.original_text + self.args.text.strip())
            print(OutputMessages.translated_morse + converter.text_to_morse(self.args.text.strip()) + "\n")
        elif self.args.validate_morse:
            print(OutputMessages.valid_morse if HelperFunctions.is_morse_valid(self.args.validate_morse.strip()) else OutputMessages.invalid_morse)
        elif self.args.user_interface:
            views.ui.main()
        else:
            print(ErrorMessages.invalid_input)
    
    @staticmethod
    def is_cli_args_valid(args: argparse.Namespace) -> bool:
        if args.validate_morse:
            if args.morse or args.text or args.user_interface:
                return False
        if (args.morse and args.text) or (args.morse and args.user_interface) or (args.text and args.user_interface) or (args.morse and args.text and args.user_interface):
            return False
        return True