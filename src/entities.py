"""
Entity repository.

Loads every YAML file inside data/entities.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml

from .model import Entity


class EntityRepository:

    def __init__(self, entities_dir: Path, ontology):

        self.entities_dir = Path(entities_dir)

        self.ontology = ontology

        self.entities: Dict[str, Entity] = {}

    def load(self):

        for file in sorted(self.entities_dir.glob("*.yaml")):

            data = yaml.safe_load(file.read_text()) or []

            for item in data:

                entity = Entity(**item)

                if entity.id in self.entities:
                    raise ValueError(
                        f"Duplicate entity: {entity.id}"
                    )

                if not self.ontology.has_class(entity.type):
                    raise ValueError(
                        f"Unknown ontology class '{entity.type}' "
                        f"for entity '{entity.id}'"
                    )

                self.entities[entity.id] = entity

    def get(self, entity_id: str) -> Entity:

        return self.entities[entity_id]

    def has(self, entity_id: str) -> bool:

        return entity_id in self.entities

