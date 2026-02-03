# Morse-Translator
A compact Morse Code ⇄ Text translator (CLI + FastAPI). This repo provides:

- Bidirectional conversions between text and Morse code (letters, numbers, common punctuation).
- Validation utilities to ensure Morse input follows allowed characters and token rules.
- A small interactive CLI plus an HTTP API (FastAPI) with versioned routes.

This README covers features, CLI usage, API endpoints (with examples), development and testing instructions.

---

## Features

- Text → Morse: converts ASCII text (letters A–Z, digits 0–9, common punctuation) to Morse code.
- Morse → Text: converts Morse code back to ASCII text; unknown tokens become `#`.
- Validation: checks Morse strings for allowed characters (only `.`, `-`, ` `, `/`) and token length rules.
- Interactive CLI: `main.py` provides a menu-driven interactive experience.
- CLI flags: single-shot conversions from the command line.
- HTTP API: FastAPI app with versioned routes (prefixed with `/v1`).

---

## Installation

1. Create a virtual environment and activate it (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r <(python - <<'PY'
from pathlib import Path
print('\n'.join([s.split('=')[0].strip().strip('"') for s in Path('pyproject.toml').read_text().splitlines() if 'dependencies' in s or s.strip().startswith('"')]))
PY
)
# Or install explicitly:
pip install fastapi uvicorn httpx requests
```

Note: the project includes `pyproject.toml` listing required packages.

Alternative venv workflows

- Using the `uv` tool: if you initialized this project with the `uv` utility and used it to create the virtual environment (for example via an `uv` init or project setup command), the venv is typically created in a `.venv` folder inside the project. Activate that venv the same way shown below for your shell (the activation commands match the venv location `./.venv`).

- Using `pipenv`:

```bash
pipenv install --dev
pipenv shell
```

- Using `poetry`:

```bash
poetry install
poetry shell
```

Activating the `.venv` (common shells and platforms)

- Linux / macOS (bash, zsh):

```bash
source .venv/bin/activate
```

- macOS (fish shell):

```fish
source .venv/bin/activate.fish
```

- Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

- Windows (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

- Git Bash / MinGW on Windows:

```bash
source .venv/Scripts/activate
```

If your venv was created in a different location by `uv` or another tool, adjust the path accordingly (for example `path/to/env/bin/activate` or `path\to\env\Scripts\activate`).

---

## Running the API server

Start the FastAPI server locally with Uvicorn:

```bash
uvicorn api.app:app --reload
```

The API will be reachable at `http://127.0.0.1:8000` and the interactive API docs at `http://127.0.0.1:8000/docs`.

Routes are versioned under `/v1` (e.g. `/v1/morse-to-text`). See the API examples below.

---

## CLI Usage (single-shot)

Run a one-off translation from the command line:

- Text to Morse:

```bash
python3 main.py -t "Hello World"
```

- Morse to Text:

```bash
python3 main.py -m ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

- Validate Morse:

```bash
python3 main.py -vm ".... . .-.. .-.. ---"
```

Notes:

- Use ` / ` (space-slash-space) to separate words in Morse. Use a single space to separate characters.
- CLI flags are mutually exclusive — use only one flag per invocation.

---

## API Endpoints and Examples

Base path: `/v1`

1) GET /v1/morse-to-text/{morse}

Example request (curl):

```bash
curl -s "http://127.0.0.1:8000/v1/morse-to-text/--"
```

Successful response (200):

```json
{"original_morse":"--","translated_morse":"M"}
```

Invalid input returns `400` with an error detail.

2) GET /v1/text-to-morse/{text}

```bash
curl -s "http://127.0.0.1:8000/v1/text-to-morse/hello"
```

Response (200):

```json
{"original_text":"hello","translated_text":".... . .-.. .-.. ---"}
```

3) GET /v1/validate-morse/{morse}

```bash
curl -s "http://127.0.0.1:8000/v1/validate-morse/--"
```

Response (200):

```json
{"original_morse":"--","is_morse_valid":true}
```

4) POST endpoints (JSON body)

- POST /v1/morse-to-text

Request body:

```json
{"morse": "-- --- .-. ... . / .. ... / ..-. ..- -."}
```

Response (200):

```json
{
  "original_morse": "-- --- .-. ... . / .. ... / ..-. ..- -.",
  "translated_morse": "MORSE IS FUN"
}
```

- POST /v1/text-to-morse

Request body:

```json
{"text": "Hello World!"}
```

Response (200):

```json
{
  "original_text": "Hello World!",
  "translated_text": ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--"
}
```

- POST /v1/validate-morse

Request body:

```json
{"morse": ".. -.- .- -.-- / -... --- -.. -.-- .-.-.-"}
```

Response (200):

```json
{
  "original_morse": ".. -.- .- -.-- / -... --- -.. -.-- .-.-.-",
  "is_morse_valid": true
}
```

Invalid POST inputs return `400` (or `200` with `is_morse_valid: false` for validation checks depending on the endpoint behavior).

---

## Validation Rules

- Allowed characters in Morse input: `.`, `-`, `/`, and space.
- Each token (space-separated) must not exceed 6 characters.
- Tokens starting with `/` must be exactly `/` (used as a word separator).

The validator lives in `utilities/utils.py` as `HelperFunctions.is_morse_valid`.

---

## Testing

Unit tests are under the `test/` directory and use `unittest` and FastAPI's `TestClient` for API tests.

Run all tests:

```bash
python3 -m unittest discover -v
```

Run a single test file:

```bash
python3 -m unittest test.api_tests
```

Notes:

- API tests use `TestClient` so you do not need to run the server to execute them.
- If you encounter unexpected failures, ensure no stray invisible Unicode characters are present in test strings (zero-width characters can cause string mismatches).

---

## Development notes

- The FastAPI app is defined in `api/app.py` and registers routes from `api/routes/v1.py`.
- Route constants and versioning live in `api/routes/routes.py` and `api/routes/versions.py`.
- Conversion logic is in `core/converters.py` and uses the dataset in `data/morse_dataset.py`.

---

## Contributing

- Bug reports and PRs are welcome. Please open an issue with repro steps and testcases.

---

## License

- MIT License

---
