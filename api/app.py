"""
FastAPI application module for Morse code translation API.

This module initializes the FastAPI application instance and registers
the v1 API routes. It serves as the main entry point for the Morse
Translator API service.

Attributes:
    app (FastAPI): The FastAPI application instance configured with v1 routes.
"""

from fastapi import FastAPI
from api.routes.v1 import router as v1_router

app = FastAPI()
app.include_router(v1_router)
