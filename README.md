# Morse-Translator
A simple Morse Code ⇄ Text translator.

## Features

- Convert plain text to Morse code (letters, digits, basic punctuation).
- Convert Morse code back to plain text.
- Interactive menu and command-line flags for single-shot conversions.
- Validate Morse code input for allowed characters and token lengths.
- Unknown characters are represented as `?` in translations.

## Quick Start

1. **Clone the repository:**
      ```bash
      git clone https://github.com/Amirhossein77-98/Python-Morse-Translator.git
      cd Python-Morse-Translator
      ```

2. **Run interactively:**

      - Linux / macOS / Termux:
         ```bash
         python3 main.py
         ```

      - Windows:
         ```powershell
         python main.py
         ```

3. **Run via CLI flags (single-shot):**

      - Translate text to Morse:
         ```bash
         python3 main.py -t "Hello World"
         # Output:
         # >>> Original Text: Hello World
         # >>> Translated Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
         ```

      - Translate Morse to text:
         ```bash
         python3 main.py -m ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
         # Output:
         # >>> Original Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
         # >>> Translated Text: Hello World
         ```

      - Validate Morse without translating:
         ```bash
         python3 main.py -vm ".... . .-.. .-.. ---"
         # Output: >>> It's Valid Morse.   (or >>> It's NOT a Valid Morse.)
         ```

## Usage notes

- For Morse input use ` / ` (space-slash-space) to separate words and a single space (` `) to separate characters.
- CLI flags are mutually exclusive: don't combine `-t` and `-m` in the same invocation.
- Use `--help` to view available CLI options.

## Examples

- Text → Morse (interactive):
   - Enter `Hello World` when prompted for Text.
   - Output: `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`

- Morse → Text (interactive):
   - Enter `.... . .-.. .-.. --- / .-- --- .-. .-.. -..` when prompted for Morse.
   - Output: `Hello World`

## Requirements

- Python 3.x

## Contributing

- Contributions, issues, and feature requests are welcome. Please open an issue or a pull request on the repository.

## License

- MIT License

---
