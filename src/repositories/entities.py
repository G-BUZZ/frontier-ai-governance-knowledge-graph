"""
Entity repository.

Loads canonical entities from data/entities.

Legacy V1 files are ignored during the migration to the
document-centric architecture.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml

from ..model import Entity


class EntityRepository:

    def __init__(self, entities_dir: Path, ontology):

        self.entities_dir = Path(entities_dir)
        self.ontology = ontology
        self.entities: Dict[str, Entity] = {}

    def load(self):

        for file in sorted(self.entities_dir.glob("*.yaml")):

            data = yaml.safe_load(file.read_text()) or []

            # Ignore legacy V1 files.
            if not isinstance(data, list):
                print(f"Skipping legacy entity file: {file.name}")
                continue

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

    def get(self, entity_id: str):

        return self.entities[entity_id]

    def has(self, entity_id: str):

        return entity_id in self.entities

