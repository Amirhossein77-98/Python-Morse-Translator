import argparse
from views.messages import OutputMessages, ErrorMessages
from core.converters import HelperFunctions

class ArgParser:
    def __init__(self):
        self.parser: argparse.ArgumentParser = argparse.ArgumentParser(description="An argument parser to use the code as cli script.")
        self.parser.add_argument('-m', '--morse', help="To enter morse directly and translate.")
        self.parser.add_argument('-t', '--text', help="To enter text directly and translate.")
        self.parser.add_argument('-vm', '--validate_morse', help="To check if a morse code is valid.")
        self.args: argparse.Namespace
    
    def parse(self) -> argparse.Namespace:
        self.args = self.parser.parse_args()
        return self.args
    
    def do_args_action(self, converter):
        if self.args.morse and HelperFunctions.is_morse_valid(self.args.morse):
            print(OutputMessages.original_morse + self.args.morse)
            print(OutputMessages.translated_text + converter.morse_to_text(self.args.morse).title() + "\n")
        elif self.args.text:
            print(OutputMessages.original_text + self.args.text)
            print(OutputMessages.translated_morse + converter.text_to_morse(self.args.text) + "\n")
        elif self.args.validate_morse:
            print(OutputMessages.valid_morse if HelperFunctions.is_morse_valid(self.args.validate_morse) else OutputMessages.invalid_morse)
        else:
            print(ErrorMessages.invalid_input)
    
    @staticmethod
    def is_cli_args_valid(args: argparse.Namespace) -> bool:
        if args.validate_morse:
            if args.morse or args.text:
                return False
        if args.morse and args.text:
            return False
        return True