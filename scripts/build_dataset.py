"""Build graph CSV files from YAML sources with ontology validation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE_DIR = PROJECT_ROOT / "data" / "sources"
GRAPH_DIR = PROJECT_ROOT / "graph"

NODES_FILE = GRAPH_DIR / "nodes.csv"
EDGES_FILE = GRAPH_DIR / "edges.csv"
NODE_TYPES_FILE = GRAPH_DIR / "node_types.csv"


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML file."""
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_valid_types() -> set[str]:
    """Load valid node types from the ontology."""
    node_types = pd.read_csv(NODE_TYPES_FILE)
    return set(node_types["type"])


def validate_nodes(nodes: list[dict[str, Any]]) -> None:
    """Validate node definitions."""

    ids: set[str] = set()
    valid_types = load_valid_types()

    for node in nodes:

        missing = {"id", "label", "type"} - node.keys()
        if missing:
            raise ValueError(
                f"Node missing fields {missing}: {node}"
            )

        if node["id"] in ids:
            raise ValueError(
                f"Duplicate node id: {node['id']}"
            )

        ids.add(node["id"])

        if node["type"] not in valid_types:
            raise ValueError(
                f"Invalid node type: {node['type']}"
            )


def validate_edges(
    edges: list[dict[str, Any]],
    node_ids: set[str],
) -> None:
    """Validate edge definitions."""

    seen = set()

    for edge in edges:

        missing = {"source", "target", "relation"} - edge.keys()
        if missing:
            raise ValueError(
                f"Edge missing fields {missing}: {edge}"
            )

        if edge["source"] not in node_ids:
            raise ValueError(
                f"Unknown source node: {edge['source']}"
            )

        if edge["target"] not in node_ids:
            raise ValueError(
                f"Unknown target node: {edge['target']}"
            )

        key = (
            edge["source"],
            edge["target"],
            edge["relation"],
        )

        if key in seen:
            raise ValueError(
                f"Duplicate edge: {key}"
            )

        seen.add(key)


def main() -> None:

    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    yaml_files = sorted(SOURCE_DIR.glob("*.yaml"))

    for path in yaml_files:
        data = load_yaml(path)

        nodes.extend(data.get("nodes", []))
        edges.extend(data.get("edges", []))

    validate_nodes(nodes)

    node_ids = {node["id"] for node in nodes}

    validate_edges(edges, node_ids)

    nodes_df = (
        pd.DataFrame(nodes)
        .sort_values(["type", "id"])
        .reset_index(drop=True)
    )

    if edges:
        edges_df = (
            pd.DataFrame(edges)
            .sort_values(["relation", "source", "target"])
            .reset_index(drop=True)
        )
    else:
        edges_df = pd.DataFrame(
            columns=["source", "target", "relation"]
        )

    GRAPH_DIR.mkdir(parents=True, exist_ok=True)

    nodes_df.to_csv(NODES_FILE, index=False)
    edges_df.to_csv(EDGES_FILE, index=False)

    print("\nDataset build complete")
    print("-" * 30)
    print(f"YAML files : {len(yaml_files)}")
    print(f"Nodes      : {len(nodes_df)}")
    print(f"Edges      : {len(edges_df)}")
    print("Validation : PASSED")


if __name__ == "__main__":
    main()
