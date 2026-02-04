
# Morse-Translator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![FastAPI](https://img.shields.io/badge/fastapi-latest-009485.svg)](https://fastapi.tiangolo.com/)
![CI](https://github.com/Amirhossein77-98/Morse-Translator/actions/workflows/ci.yml/badge.svg)

- [نسخه فارسی سند](../docs/README.fa.md)
- [النسخة العربية من المستند](../docs/README.ar.md)
- [Version française du document](../docs/README.fr.md)

A compact, feature-rich Morse Code ⇄ Text translator with CLI, GUI, and REST API. Bidirectional conversions for letters, numbers, and common punctuation with built-in validation.

---

## 📸 Screenshots

<div style="
  display:flex;
  gap:12px;
  overflow-x:auto;
  padding:12px 0;
  flex-wrap:nowrap;
">
  <img src="screenshots/1.png" style="max-height:420px; flex:0 0 auto;">
  <img src="screenshots/2.png" style="max-height:420px; flex:0 0 auto;">
  <img src="screenshots/3.png" style="max-height:420px; flex:0 0 auto;">
  <img src="screenshots/4.png" style="max-height:420px; flex:0 0 auto;">
  <img src="screenshots/5.png" style="max-height:420px; flex:0 0 auto;">
</div>

---

## 🚀 Features

- **Text ↔ Morse**: bidirectional conversion for A–Z, 0–9, and common punctuation
- **Validation**: checks Morse syntax (allowed: `.`, `-`, `/`, space; max 6 chars per token)
- **Interactive CLI**: menu-driven experience via `main.py`
- **Desktop GUI**: responsive `customtkinter`-based UI with text/Morse input fields and toggle switch
- **REST API**: FastAPI with versioned routes (`/v1`) and interactive docs at `/docs`
- **Installable package**: global `morse` command after `pip install -e .`
- **CLI flags**: single-shot conversions (`-t`, `-m`, `-vm`, `-ui`)

---

## 📦 Installation

1. **Clone and create virtual environment:**

```bash
git clone https://github.com/amirhossein77-98/Morse-Translator.git
cd Morse-Translator
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. **Install dependencies:**

```bash
pip install -e .
```

Installs the project in development mode with the global `morse` CLI entry point.

**Alternative environments:**
- **pipenv:** `pipenv install --dev && pipenv shell`
- **poetry:** `poetry install && poetry shell`
- **uv:** `uv sync` (if initialized with uv)

---

## 🖥 Usage

### Direct run

**Interactive menu:**
```bash
python3 main.py
```

### CLI args

All flags are mutually exclusive. Use ` / ` (space-slash-space) to separate words in Morse.

**Text to Morse:**
```bash
python3 main.py -t "Hello World"
morse -t "Hello World"  # After pip install -e .
```

**Morse to Text:**
```bash
python3 main.py -m ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

**Validate Morse:**
```bash
python3 main.py -vm ".... . .-.. .-.. ---"
```

### GUI

Launch the responsive `customtkinter` GUI:

```bash
python3 main.py -ui
morse -ui  # After pip install -e .
```

**Features:**
- Toggle between "Text to Morse" and "Morse to Text" via switch
- Real-time input/output textboxes
- Validation for Morse input
- Responsive grid layout, centered widgets

### API

Start the FastAPI server:

```bash
uvicorn api.app:app --reload
```

Open `http://127.0.0.1:8000/docs` for interactive API docs.

**Example endpoints** (base: `/v1`):

```bash
# GET
curl "http://127.0.0.1:8000/v1/text-to-morse/hello"
curl "http://127.0.0.1:8000/v1/morse-to-text/--"
curl "http://127.0.0.1:8000/v1/validate-morse/--"

# POST
curl -X POST "http://127.0.0.1:8000/v1/text-to-morse" \
  -H "Content-Type: application/json" \
  -d '{"text":"hello"}'
```

Response format:
```json
{
  "original_text": "hello",
  "translated_text": ".... . .-.. .-.. ---"
}
```

### Installable `morse` package

After `pip install -e .`, use the global `morse` command:

```bash
morse -t "Hello"
morse -m ".... . .-.. .-.. ---"
morse -vm "..."
morse -ui
```

---

## 🔧 Testing

Run unit and API tests (no server startup needed):

```bash
python3 -m unittest discover -v        # All tests
python3 -m unittest test.api_tests     # API only
python3 -m unittest test.converter_tests  # Converter only
```

**Note:** Tests use `unittest` and FastAPI `TestClient`. Ensure no stray Unicode characters in test strings.

---

## 🛠 Packaging & Contributing

**Build distribution packages:**

```bash
pip install build
python -m build
```

Creates wheels and source distributions in `dist/`.

**Project structure:**
- `core/converters.py` — conversion logic & validation
- `data/morse_dataset.py` — Morse/ASCII mapping
- `api/app.py` — FastAPI application
- `api/routes/v1.py` — versioned endpoints
- `views/ui/ctkinter_ui.py` — GUI with `customtkinter`
- `test/` — unit and API tests

**Contributing:**
Bug reports and PRs welcome. Please include repro steps and test cases.

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.
