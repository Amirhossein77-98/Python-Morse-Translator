from fastapi import FastAPI, HTTPException, status
from core.converters import Converters
from views.messages import AppName, APIMessages, ErrorMessages
from utilities.utils import HelperFunctions
from api.schemas import TextRequest, MorseRequest
from api.routes.routes import MorseToText, TextToMorse, MorseValidation, Root, HealthCheck
from api.routes.versions import CurrentVersion

app = FastAPI()
converter: Converters = Converters()

# GET Routes
@app.get(CurrentVersion.current_version_route+Root.route)
def root():
    return {
        "api_version": CurrentVersion.current_version_declaration,
        "message": AppName.app_name
        }

@app.get(CurrentVersion.current_version_route+HealthCheck.route)
def health_check():
    return {APIMessages.api_status: APIMessages.api_health_ok}

@app.get(CurrentVersion.current_version_route+MorseToText.route+'/{morse}')
def morse_to_text(morse: str):
    morse = morse.strip()
    if HelperFunctions.is_morse_valid(morse):
        return {
            APIMessages.api_original_morse_key: morse,
            APIMessages.api_translated_morse_key: converter.morse_to_text(morse)
            }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_morse_input)

@app.get(CurrentVersion.current_version_route+TextToMorse.route+'/{text}')
def text_to_morse(text: str):
    text = text.strip()
    if len(text) != 0:
        return {
            APIMessages.api_original_text_key: text,
            APIMessages.api_translated_text_key: converter.text_to_morse(text)
        }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_input)

@app.get(CurrentVersion.current_version_route+MorseValidation.route+'/{morse}')
def validate_morse(morse: str):
    morse = morse.strip()
    return {
        APIMessages.api_original_morse_key: morse,
        APIMessages.api_morse_validation_check_key: HelperFunctions.is_morse_valid(morse)
    }

# POST Routs
@app.post(CurrentVersion.current_version_route+MorseToText.route)
def morse_to_text_post(body: MorseRequest):
    morse = body.morse.strip()
    if HelperFunctions.is_morse_valid(morse):
        return {
            APIMessages.api_original_morse_key: morse,
            APIMessages.api_translated_morse_key: converter.morse_to_text(morse)
            }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_morse_input)

@app.post(CurrentVersion.current_version_route+TextToMorse.route)
def text_to_morse_post(body: TextRequest):
    text = body.text.strip()
    if len(text) != 0:
        return {
            APIMessages.api_original_text_key: text,
            APIMessages.api_translated_text_key: converter.text_to_morse(text)
        }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_input)

@app.post(CurrentVersion.current_version_route+MorseValidation.route)
def validate_morse_post(body: MorseRequest):
    morse = body.morse.strip()
    return {
        APIMessages.api_original_morse_key: morse,
        APIMessages.api_morse_validation_check_key: HelperFunctions.is_morse_valid(morse)
    }
