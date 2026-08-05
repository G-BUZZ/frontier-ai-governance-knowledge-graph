"""Export graph CSV files to a single YAML dataset."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent

GRAPH_DIR = PROJECT_ROOT / "graph"
SOURCE_DIR = PROJECT_ROOT / "data" / "sources"

NODES_FILE = GRAPH_DIR / "nodes.manual.csv"
EDGES_FILE = GRAPH_DIR / "edges.manual.csv"

OUTPUT_FILE = SOURCE_DIR / "all.yaml"


def main() -> None:
    """Export nodes and edges from CSV to YAML."""

    nodes = pd.read_csv(NODES_FILE).to_dict(orient="records")
    edges = pd.read_csv(EDGES_FILE).to_dict(orient="records")

    SOURCE_DIR.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        yaml.safe_dump(
            {
                "nodes": nodes,
                "edges": edges,
            },
            f,
            sort_keys=False,
            allow_unicode=True,
        )

    print("YAML export complete")
    print(f"Nodes : {len(nodes)}")
    print(f"Edges : {len(edges)}")
    print(f"File  : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
