"""
Pydantic schemas for morse code translation API requests.

This module defines the request body schemas for the morse code translator API endpoints.
It uses Pydantic's BaseModel for data validation and serialization.

Classes:
    TextRequest: Schema for requests containing plain text to be translated to morse code.
    MorseRequest: Schema for requests containing morse code to be translated to plain text.
"""

from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class MorseRequest(BaseModel):
    morse: str