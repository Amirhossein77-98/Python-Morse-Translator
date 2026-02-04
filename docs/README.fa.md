# مترجم مورس

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![FastAPI](https://img.shields.io/badge/fastapi-latest-009485.svg)](https://fastapi.tiangolo.com/)
[![PyPI version](https://img.shields.io/pypi/v/amirstein-morse-translator.svg)](https://pypi.org/project/amirstein-morse-translator/)
![CI](https://github.com/Amirhossein77-98/Morse-Translator/actions/workflows/ci.yml/badge.svg)

- [النسخة العربية من المستند](../docs/README.ar.md)
- [English Version of the Doc](../README.md)
- [Version française du document](../docs/README.fr.md)

یک مترجم مختصر و پر امکانات کد مورس ⇄ متن با رابط خط فرمان، رابط گرافیکی و رابط REST API. تبدیل دو طرفه برای حروف، 
اعداد و نشانه‌گذاری رایج با اعتبارسنجی داخلی.

---

## 📸 تصاویر

<div style="
  display:flex;
  gap:12px;
  overflow-x:auto;
  padding:12px 0;
  flex-wrap:nowrap;
">
  <img src="../screenshots/1.png" style="max-height:420px; flex:0 0 auto;">
  <img src="../screenshots/2.png" style="max-height:420px; flex:0 0 auto;">
  <img src="../screenshots/3.png" style="max-height:420px; flex:0 0 auto;">
  <img src="../screenshots/4.png" style="max-height:420px; flex:0 0 auto;">
  <img src="../screenshots/5.png" style="max-height:420px; flex:0 0 auto;">
</div>

---

## 🚀 ویژگی‌ها

- **متن ↔ مورس**: تبدیل دو طرفه برای حروف A–Z، اعداد 0–9 و نشانه‌گذاری رایج
- **اعتبارسنجی**: بررسی نحو مورس (اجازه: `.`, `-`, `/`, فاصله؛ حداکثر 6 کاراکتر در هر توکن)
- **رابط خط فرمان تعاملی**: تجربه منو مبتنی بر `main.py`
- **رابط گرافیکی دسکتاپ**: رابط کاربری پاسخگو مبتنی بر `customtkinter` با فیلدهای ورودی متن/مورس و کلید تغییر وضعیت
- **REST API**: FastAPI با مسیرهای نسخه بندی‌شده (`/v1`) و مستندات تعاملی در `/docs`
- **نصب‌پذیر**: فرمان global `morse` پس از `pip install -e .`
- **علامت‌نشان CLI**: تبدیل‌های یک‌بار مصرف (`-t`, `-m`, `-vm`, `-ui`)

---

## 🔧 نصب

1. **کپی کردن مخزن و ایجاد محیط مجازی:**

```bash
git clone https://github.com/amirhossein77-98/Morse-Translator.git
cd Morse-Translator
python3 -m venv .venv
source .venv/bin/activate  # روی ویندوز: .venv\Scripts\activate
```

2. **نصب وابستگی‌ها:**

```bash
pip install -e .
# نصب پروژه در حالت توسعه با نقطه ورودی CLI `morse`
```

### محیط‌های جایگزین

```bash
# با Poetry
poetry install
poetry shell
# با Pipenv
pipenv install
pipenv shell
# با Conda
conda create -n morse python=3.10
conda activate morse
conda install pip
pip install -e .
```

---

## 💻 استفاده

### اجرای مستقیم

**منوی تعاملی:**
```bash
python3 main.py
```

### آرگومان‌های CLI

تمام پرچم‌ها به صورت تبادلی (mutually exclusive) هستند. برای جدا کردن کلمات در مورس از ` / ` (فاصله-اسلش-فاصله) استفاده 
کنید.

**متن به مورس:**
```bash
python3 main.py -t "Hello World"
morse -t "Hello World"  # بعد از pip install -e .
```

**مورس به متن:**
```bash
python3 main.py -m ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

**اعتبارسنجی مورس:**
```bash
python3 main.py -vm ".... . .-.. .-.. ---"
```

### رابط گرافیکی

GUI واکنش‌گرا مبتنی بر `customtkinter` را اجرا کنید:

```bash
python3 main.py -ui
morse -ui  # بعد از pip install -e .
```

#### ویژگی‌ها

- تغییر بین «متن به مورس» و «مورس به متن» از طریق کلید تغییر وضعیت
- جعبه‌های ورودی/خروجی به‌صورت لحظه‌ای
- اعتبارسنجی ورودی مورس
- طرح شبکه‌ای پاسخگو، ویجت‌های مرکز شده

### API

سرور FastAPI را اجرا کنید:

```bash
uvicorn api.app:app --reload
```

باز کردن `http://127.0.0.1:8000/docs` برای مستندات تعاملی API.

**نمونه مسیرها** (پایه: `/v1`):

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

فرمت پاسخ:
```json
{
  "original_text": "hello",
  "translated_text": ".... . .-.. .-.. ---"
}
```

### بسته نصب‌پذیر `morse`

پس از `pip install -e .`، از فرمان global `morse` استفاده کنید:

```bash
morse -t "Hello"
morse -m ".... . .-.. .-.. ---"
morse -vm "..."
morse -ui
```

---

## 🔧 تست

تست واحد و API را بدون نیاز به راه‌اندازی سرور اجرا کنید:

```bash
python3 -m unittest discover -v        # تمام تست‌ها
python3 -m unittest test.api_tests     # فقط API
python3 -m unittest test.converter_tests  # فقط کنتور
```

> توجه: تست‌ها از `unittest` و FastAPI `TestClient` استفاده می‌کنند. مطمئن شوید که هیچ کاراکتر یونی‌کد اضافی در رشته‌های 
تست وجود ندارد.

---

## 🛠 بسته‌بندی و مشارکت

**ساخت بسته‌های توزیع:**

```bash
pip install build
python -m build
```

این دستورات wheel و توزیع منبع را در `dist/` ایجاد می‌کند.

**ساختار پروژه:**

- `core/converters.py` — منطق تبدیل و اعتبارسنجی
- `data/morse_dataset.py` — نقشه‌برداری مورس/ASCII
- `api/app.py` — برنامه FastAPI
- `api/routes/v1.py` — مسیرهای نسخه بندی‌شده
- `views/ui/ctkinter_ui.py` — رابط گرافیکی با `customtkinter`
- `test/` — تست‌های واحد و API

> گزارش‌های خطا و PRs مورد استقبال است. لطفاً گام‌های بازتولید و موارد تست را شامل کنید.

---

## 📜 مجوز

مجوز MIT — برای جزئیات، به [LICENSE](LICENSE) مراجعه کنید.