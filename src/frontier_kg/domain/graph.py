"""
Knowledge Graph aggregate.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .assertion import Assertion
from .document import SourceDocument
from .entity import Entity
from .ontology import OntologyClass, RelationType


@dataclass(slots=True)
class KnowledgeGraph:

    ontology_classes: dict[str, OntologyClass] = field(default_factory=dict)

    relation_types: dict[str, RelationType] = field(default_factory=dict)

    entities: dict[str, Entity] = field(default_factory=dict)

    documents: dict[str, SourceDocument] = field(default_factory=dict)

    assertions: list[Assertion] = field(default_factory=list)
