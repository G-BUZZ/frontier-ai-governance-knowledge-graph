#!/usr/bin/env python3
"""
Frontier AI Governance Knowledge Graph
=====================================

Main build entrypoint.

Pipeline

    ontology
        ↓
    entities
        ↓
    assertions
        ↓
    validation
        ↓
    graph export

This file intentionally contains almost no business logic.
All logic lives inside the src package.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent

sys.path.insert(0, str(ROOT))

from src.builder import KnowledgeGraphBuilder


def main():

    builder = KnowledgeGraphBuilder(
        ontology_dir=ROOT / "data" / "ontology",
        entities_dir=ROOT / "data" / "entities",
        assertions_dir=ROOT / "data" / "assertions",
        output_dir=ROOT / "graph",
    )

    builder.build()


if __name__ == "__main__":
    main()

