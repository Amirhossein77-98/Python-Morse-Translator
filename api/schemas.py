from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class MorseRequest(BaseModel):
    morse: str