"""
Assertion model.

Assertions are evidence-backed statements extracted from documents.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class Provenance:

    document: str

    page: str | None = None

    section: str | None = None

    quote: str | None = None

    confidence: float = 1.0

    notes: str | None = None


@dataclass(slots=True, frozen=True)
class Assertion:

    id: str

    subject: str

    predicate: str

    object: str

    provenance: Provenance

    qualifiers: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):

        if not self.id:
            raise ValueError("Assertion id cannot be empty.")
