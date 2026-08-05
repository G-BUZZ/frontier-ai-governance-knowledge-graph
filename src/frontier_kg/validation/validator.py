"""
Main validation entry point.
"""

from __future__ import annotations

from pathlib import Path

from .layout import LayoutValidator
from .result import ValidationResult


class Validator:

    def __init__(self, data_dir: Path):

        self.data_dir = Path(data_dir)

    def validate(self) -> ValidationResult:

        result = ValidationResult()

        validators = [
            LayoutValidator(self.data_dir),
        ]

        for validator in validators:

            partial = validator.validate()

            result.errors.extend(partial.errors)

        return result
