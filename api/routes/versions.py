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