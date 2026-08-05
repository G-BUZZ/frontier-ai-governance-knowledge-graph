"""Validate ontology definitions used by the knowledge graph."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

NODE_TYPES = PROJECT_ROOT / "graph" / "node_types.csv"
RELATION_TYPES = PROJECT_ROOT / "graph" / "relation_types.csv"


def main() -> None:
    node_types = pd.read_csv(NODE_TYPES)
    relation_types = pd.read_csv(RELATION_TYPES)

    valid_types = set(node_types["type"])

    print("Ontology Validation")
    print("-" * 40)

    print(f"Node types      : {len(node_types)}")
    print(f"Relation types  : {len(relation_types)}")

    errors = 0

    for row in relation_types.itertuples(index=False):

        if row.source_type not in valid_types:
            print(
                f"ERROR: unknown source type '{row.source_type}'"
            )
            errors += 1

        if row.target_type not in valid_types:
            print(
                f"ERROR: unknown target type '{row.target_type}'"
            )
            errors += 1

    if errors == 0:
        print("Ontology validation PASSED")
    else:
        raise SystemExit(
            f"Ontology validation FAILED ({errors} errors)"
        )


if __name__ == "__main__":
    main()
