from dataclasses import dataclass

@dataclass
class VersionOne():
    route: str = '/v1'

@dataclass
class CurrentVersion():
    current_version_declaration: str = "Version 1"
    current_version_route: str = VersionOne.route