"""
Source document model.

Documents are primary evidence.

Assertions always reference one source document.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class SourceDocument:

    id: str

    title: str

    publisher: str

    publication_date: str

    url: str

    document_type: str

    version: str = ""

    language: str = "en"

    license: str = ""

    description: str = ""

    tags: list[str] = field(default_factory=list)

    def __post_init__(self):

        if not self.id:
            raise ValueError("Document id cannot be empty.")

        if not self.title:
            raise ValueError("Document title cannot be empty.")
