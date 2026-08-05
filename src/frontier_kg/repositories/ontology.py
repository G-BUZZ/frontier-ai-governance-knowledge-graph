"""
Ontology repository.

Loads ontology classes and relation types from YAML.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from frontier_kg.domain.ontology import (
    OntologyClass,
    RelationType,
)


class OntologyRepository:

    def __init__(self, ontology_dir: Path):

        self.ontology_dir = Path(ontology_dir)

        self.classes: dict[str, OntologyClass] = {}
        self.relations: dict[str, RelationType] = {}

    def load(self):

        self._load_classes()
        self._load_relations()

    def _load_classes(self):

        file = self.ontology_dir / "classes.yaml"

        data = yaml.safe_load(file.read_text()) or []

        for item in data:

            ontology_class = OntologyClass(**item)

            if ontology_class.id in self.classes:
                raise ValueError(
                    f"Duplicate ontology class '{ontology_class.id}'"
                )

            self.classes[ontology_class.id] = ontology_class

    def _load_relations(self):

        file = self.ontology_dir / "relations.yaml"

        data = yaml.safe_load(file.read_text()) or []

        for item in data:

            relation = RelationType(**item)

            if relation.id in self.relations:
                raise ValueError(
                    f"Duplicate relation '{relation.id}'"
                )

            self.relations[relation.id] = relation

    def has_class(self, class_id: str) -> bool:
        return class_id in self.classes

    def has_relation(self, relation_id: str) -> bool:
        return relation_id in self.relations

    def get_class(self, class_id: str) -> OntologyClass:
        return self.classes[class_id]

    def get_relation(self, relation_id: str) -> RelationType:
        return self.relations[relation_id]
