"""
Assertion repository.

Loads document-centric assertions and validates
their references against ontology, entities and documents.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from frontier_kg.domain.assertion import Assertion, Provenance
from frontier_kg.repositories.documents import DocumentRepository
from frontier_kg.repositories.entities import EntityRepository
from frontier_kg.repositories.ontology import OntologyRepository


class AssertionRepository:

    def __init__(
        self,
        assertions_dir: Path,
        entities: EntityRepository,
        documents: DocumentRepository,
        ontology: OntologyRepository,
    ):

        self.assertions_dir = Path(assertions_dir)

        self.entities = entities
        self.documents = documents
        self.ontology = ontology

        self.assertions: list[Assertion] = []

    def load(self):

        for file in sorted(self.assertions_dir.glob("*.yaml")):

            data = yaml.safe_load(file.read_text())

            document_id = data["document"]

            if not self.documents.has(document_id):
                raise ValueError(
                    f"Unknown document '{document_id}'"
                )

            for item in data.get("assertions", []):

                if not self.entities.has(item["subject"]):
                    raise ValueError(
                        f"Unknown subject '{item['subject']}'"
                    )

                if not self.entities.has(item["object"]):
                    raise ValueError(
                        f"Unknown object '{item['object']}'"
                    )

                if not self.ontology.has_relation(item["predicate"]):
                    raise ValueError(
                        f"Unknown relation '{item['predicate']}'"
                    )

                provenance = Provenance(**item["provenance"])

                assertion = Assertion(
                    id=item["id"],
                    subject=item["subject"],
                    predicate=item["predicate"],
                    object=item["object"],
                    provenance=provenance,
                    qualifiers=item.get("qualifiers", {}),
                )

                self.assertions.append(assertion)
