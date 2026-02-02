from fastapi import APIRouter, HTTPException, status
from core.converters import Converters
from views.messages import AppName, APIMessages, ErrorMessages
from utilities.utils import HelperFunctions
from api.schemas import TextRequest, MorseRequest
from api.routes.routes import MorseToText, TextToMorse, MorseValidation, Root, HealthCheck
from api.routes.versions import CurrentVersion

router = APIRouter(
                    prefix=CurrentVersion.current_version_route,
                    tags=[CurrentVersion.current_version_tagging]
                    )
converter: Converters = Converters()


# GET Routes
@router.get(Root.route)
def root():
    return {
        "api_version": CurrentVersion.current_version_declaration,
        "message": AppName.app_name
        }

@router.get(HealthCheck.route)
def health_check():
    return {APIMessages.api_status: APIMessages.api_health_ok}

@router.get(MorseToText.route+'/{morse}')
def morse_to_text(morse: str):
    morse = morse.strip()
    if HelperFunctions.is_morse_valid(morse):
        return {
            APIMessages.api_original_morse_key: morse,
            APIMessages.api_translated_morse_key: converter.morse_to_text(morse)
            }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_morse_input)

@router.get(TextToMorse.route+'/{text}')
def text_to_morse(text: str):
    text = text.strip()
    if len(text) != 0:
        return {
            APIMessages.api_original_text_key: text,
            APIMessages.api_translated_text_key: converter.text_to_morse(text)
        }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_input)

@router.get(MorseValidation.route+'/{morse}')
def validate_morse(morse: str):
    morse = morse.strip()
    return {
        APIMessages.api_original_morse_key: morse,
        APIMessages.api_morse_validation_check_key: HelperFunctions.is_morse_valid(morse)
    }

# POST Routs
@router.post(MorseToText.route)
def morse_to_text_post(body: MorseRequest):
    morse = body.morse.strip()
    if HelperFunctions.is_morse_valid(morse):
        return {
            APIMessages.api_original_morse_key: morse,
            APIMessages.api_translated_morse_key: converter.morse_to_text(morse)
            }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_morse_input)

@router.post(TextToMorse.route)
def text_to_morse_post(body: TextRequest):
    text = body.text.strip()
    if len(text) != 0:
        return {
            APIMessages.api_original_text_key: text,
            APIMessages.api_translated_text_key: converter.text_to_morse(text)
        }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorMessages.invalid_input)

@router.post(MorseValidation.route)
def validate_morse_post(body: MorseRequest):
    morse = body.morse.strip()
    return {
        APIMessages.api_original_morse_key: morse,
        APIMessages.api_morse_validation_check_key: HelperFunctions.is_morse_valid(morse)
    }
