"""
Document repository.

Loads source document metadata from YAML files.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from frontier_kg.domain.document import SourceDocument


class DocumentRepository:

    def __init__(self, documents_dir: Path):

        self.documents_dir = Path(documents_dir)

        self.documents: dict[str, SourceDocument] = {}

    def load(self):

        for file in sorted(self.documents_dir.glob("*.yaml")):

            data = yaml.safe_load(file.read_text())

            document = SourceDocument(**data)

            if document.id in self.documents:

                raise ValueError(
                    f"Duplicate document '{document.id}'"
                )

            self.documents[document.id] = document

    def has(self, document_id: str):

        return document_id in self.documents

    def get(self, document_id: str):

        return self.documents[document_id]
