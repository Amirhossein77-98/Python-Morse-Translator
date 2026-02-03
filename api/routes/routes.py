"""
Route definitions for the Morse Translator API.

This module defines dataclass-based route endpoints for the Morse Translator application.
Each route class represents a specific API endpoint with its corresponding path.

Classes:
    Root: The root endpoint of the API.
    HealthCheck: Health check endpoint to verify API availability.
    TextToMorse: Endpoint for converting text to Morse code.
    MorseToText: Endpoint for converting Morse code to text.
    MorseValidation: Endpoint for validating Morse code format.
"""

from dataclasses import dataclass

@dataclass
class Root():
    route: str = '/'

@dataclass
class HealthCheck():
    route: str = '/health'

@dataclass
class TextToMorse():
    route: str = '/text-to-morse'

@dataclass
class MorseToText():
    route: str = '/morse-to-text'

@dataclass
class MorseValidation():
    route: str = '/validate-morse'