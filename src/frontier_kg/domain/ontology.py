"""
Ontology model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class OntologyClass:

    id: str

    label: str

    description: str = ""

    parent: str | None = None


@dataclass(slots=True, frozen=True)
class RelationType:

    id: str

    label: str

    domain: str

    range: str

    description: str = ""
