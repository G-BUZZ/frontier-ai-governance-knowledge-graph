"""
Document repository.

Loads every metadata document stored in data/documents.
"""

from pathlib import Path

import yaml

from .model import SourceDocument


class DocumentRepository:

    def __init__(self, documents_dir):

        self.documents_dir = Path(documents_dir)

        self.documents = {}

    def load(self):

        for file in sorted(self.documents_dir.glob("*.yaml")):

            data = yaml.safe_load(file.read_text())

            document = SourceDocument(**data)

            if document.id in self.documents:
                raise ValueError(
                    f"Duplicate document '{document.id}'"
                )

            self.documents[document.id] = document

    def has(self, document_id):

        return document_id in self.documents

    def get(self, document_id):

        return self.documents[document_id]

