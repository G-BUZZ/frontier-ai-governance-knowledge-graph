"""
Canonical entity model.

Entities represent stable real-world concepts in the Frontier AI
Governance Knowledge Graph.

Examples
--------
- Anthropic
- OpenAI
- Claude Opus 4
- EU AI Act
- ARC-AGI
- Responsible Scaling Policy

Entities are intentionally independent from source documents.

Documents make assertions *about* entities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class Entity:

    id: str

    type: str

    label: str

    aliases: list[str] = field(default_factory=list)

    description: str = ""

    attributes: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):

        if not self.id:
            raise ValueError("Entity id cannot be empty.")

        if not self.type:
            raise ValueError("Entity type cannot be empty.")

        if not self.label:
            raise ValueError("Entity label cannot be empty.")
