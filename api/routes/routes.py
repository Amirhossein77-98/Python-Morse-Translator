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