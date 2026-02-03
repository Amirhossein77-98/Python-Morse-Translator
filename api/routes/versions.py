"""
Module for managing API version information.

This module defines version-specific configurations used throughout the API,
including route paths, version declarations, and version tags.

Classes:
    VersionOne: Dataclass containing Version 1 API configuration.
    CurrentVersion: Dataclass that references the current active API version settings.
"""

from dataclasses import dataclass

@dataclass
class VersionOne():
    route: str = '/v1'
    declaration: str = "Version 1"
    tagging: str = "v1"

@dataclass
class CurrentVersion():
    current_version_declaration: str = VersionOne.declaration
    current_version_tagging: str = VersionOne.tagging
    current_version_route: str = VersionOne.route