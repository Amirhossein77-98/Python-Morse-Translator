from fastapi import FastAPI, HTTPException, status
from core.converters import Converters
from views.messages import AppName, APIMessages, ErrorMessages
from utilities.utils import HelperFunctions

app = FastAPI()
converter: Converters = Converters()

@app.get('/')
def root():
    return {"message": AppName.app_name}

@app.get('/health')
def health_check():
    return {APIMessages.api_status: APIMessages.api_health_ok}

@app.get('/morse-to-text/{morse}')
def morse_to_text(morse: str):
    morse = morse.strip()
    if HelperFunctions.is_morse_valid(morse):
        return {
            APIMessages.api_original_morse_key: morse,
            APIMessages.api_translated_morse_key: converter.morse_to_text(morse)
            }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_morse_input)

@app.get('/text-to-morse/{text}')
def text_to_morse(text: str):
    text = text.strip()
    if len(text) != 0:
        return {
            APIMessages.api_original_text_key: text,
            APIMessages.api_translated_text_key: converter.text_to_morse(text)
        }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_input)

@app.get('/validate-morse/{morse}')
def validate_morse(morse: str):
    morse.strip()
    return {
        APIMessages.api_original_morse_key: morse,
        APIMessages.api_morse_validation_check_key: HelperFunctions.is_morse_valid(morse)
    }
