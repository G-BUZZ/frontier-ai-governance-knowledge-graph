"""
Entity repository.

Loads canonical entities from YAML files.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from frontier_kg.domain.entity import Entity
from frontier_kg.repositories.ontology import OntologyRepository


class EntityRepository:

    def __init__(
        self,
        entities_dir: Path,
        ontology: OntologyRepository,
    ):

        self.entities_dir = Path(entities_dir)

        self.ontology = ontology

        self.entities: dict[str, Entity] = {}

    def load(self):

        for file in sorted(self.entities_dir.glob("*.yaml")):

            data = yaml.safe_load(file.read_text()) or []

            for item in data:

                entity = Entity(**item)

                if entity.id in self.entities:
                    raise ValueError(
                        f"Duplicate entity '{entity.id}'"
                    )

                if not self.ontology.has_class(entity.type):
                    raise ValueError(
                        f"Unknown ontology class '{entity.type}'"
                    )

                self.entities[entity.id] = entity

    def has(self, entity_id: str):

        return entity_id in self.entities

    def get(self, entity_id: str):

        return self.entities[entity_id]
