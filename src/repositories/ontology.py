"""
Ontology repository.

Loads ontology classes and relation types.

Directory structure:

data/
    ontology/
        classes.yaml
        relations.yaml

The repository exposes an immutable view of the ontology
used by the rest of the application.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml

from .model import OntologyClass, RelationType


class OntologyRepository:

    def __init__(self, ontology_dir: Path):

        self.ontology_dir = Path(ontology_dir)

        self.classes: Dict[str, OntologyClass] = {}

        self.relations: Dict[str, RelationType] = {}

    # ---------------------------------------------------------

    def load(self):

        self._load_classes()

        self._load_relations()

    # ---------------------------------------------------------

    def _load_classes(self):

        path = self.ontology_dir / "classes.yaml"

        if not path.exists():
            raise FileNotFoundError(path)

        data = yaml.safe_load(path.read_text())

        for item in data:

            cls = OntologyClass(**item)

            if cls.id in self.classes:
                raise ValueError(
                    f"Duplicate ontology class: {cls.id}"
                )

            self.classes[cls.id] = cls

    # ---------------------------------------------------------

    def _load_relations(self):

        path = self.ontology_dir / "relations.yaml"

        if not path.exists():
            raise FileNotFoundError(path)

        data = yaml.safe_load(path.read_text())

        for item in data:

            relation = RelationType(**item)

            if relation.id in self.relations:
                raise ValueError(
                    f"Duplicate relation: {relation.id}"
                )

            self.relations[relation.id] = relation

    # ---------------------------------------------------------

    def has_class(self, class_id: str) -> bool:

        return class_id in self.classes

    def has_relation(self, relation_id: str) -> bool:

        return relation_id in self.relations

    def get_class(self, class_id: str) -> OntologyClass:

        return self.classes[class_id]

    def get_relation(self, relation_id: str) -> RelationType:

        return self.relations[relation_id]

