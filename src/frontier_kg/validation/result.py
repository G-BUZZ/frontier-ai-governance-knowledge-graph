"""
Validation result objects.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ValidationError:

    location: str

    message: str


@dataclass(slots=True)
class ValidationResult:

    errors: list[ValidationError] = field(default_factory=list)

    @property
    def valid(self) -> bool:

        return len(self.errors) == 0

    def add(self, location: str, message: str):

        self.errors.append(
            ValidationError(location, message)
        )
