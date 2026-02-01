from models.converters import Converters
from views.messages import OutputMessages, AppName
from models.cli_args_handler import ArgParser
from models.interactive_cli_env import InteractiveCLIEnvironment

def main():
    """
    Main entry point for the Morse Translator application.
    Initializes the converter and argument parser, then routes execution based on:
    - Command-line arguments (morse, text, or validate_morse flags)
    - Interactive mode if no arguments are provided
    Validates CLI arguments before execution and displays appropriate error messages
    if invalid input is detected. Falls back to interactive CLI environment for
    user-friendly interaction when no CLI arguments are specified.
    Raises:
        SystemExit: If invalid CLI arguments are provided.
    """

    converter = Converters()
    arg_parser = ArgParser()
    args = arg_parser.parse()
    
    print(f"\n{'*'*5} {AppName.app_name} {'*'*5} \n")
    
    if args.morse or args.text or args.validate_morse:
        if (ArgParser.is_cli_args_valid(args)):
            arg_parser.do_args_action(converter)
        else:
            print(OutputMessages.invalid_input_get_cli_help)
    else:
        interactive_app_env: InteractiveCLIEnvironment = InteractiveCLIEnvironment(converter)
        interactive_app_env.run()

if __name__ == "__main__":
    main()