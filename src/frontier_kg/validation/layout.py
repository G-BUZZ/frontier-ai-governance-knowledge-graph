"""
Repository layout validator.

Checks that the expected project data layout exists.
"""

from __future__ import annotations

from pathlib import Path

from .result import ValidationResult


class LayoutValidator:

    REQUIRED_DIRECTORIES = (
        "ontology",
        "entities",
        "documents",
        "assertions",
    )

    def __init__(self, data_dir: Path):

        self.data_dir = Path(data_dir)

    def validate(self) -> ValidationResult:

        result = ValidationResult()

        if not self.data_dir.exists():
            result.add("data", "Data directory does not exist.")
            return result

        for directory in self.REQUIRED_DIRECTORIES:

            path = self.data_dir / directory

            if not path.exists():
                result.add(
                    directory,
                    f"Missing required directory '{directory}'.",
                )
                continue

            if not path.is_dir():
                result.add(
                    directory,
                    f"'{directory}' is not a directory.",
                )

        return result
