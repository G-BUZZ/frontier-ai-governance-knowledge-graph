"""Build and export the Frontier AI Governance Knowledge Graph.

This module loads node and edge definitions from CSV files, validates their
structure, builds a NetworkX MultiDiGraph, and exports the graph in multiple
formats.

Outputs:
    - outputs/graph.graphml
    - outputs/graph.gexf
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

import networkx as nx
import pandas as pd

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent

GRAPH_DIR: Final[Path] = PROJECT_ROOT / "graph"
OUTPUT_DIR: Final[Path] = PROJECT_ROOT / "outputs"

NODES_FILE: Final[Path] = GRAPH_DIR / "nodes.csv"
EDGES_FILE: Final[Path] = GRAPH_DIR / "edges.csv"

GRAPHML_FILE: Final[Path] = OUTPUT_DIR / "graph.graphml"
GEXF_FILE: Final[Path] = OUTPUT_DIR / "graph.gexf"

# -----------------------------------------------------------------------------
# Required schema
# -----------------------------------------------------------------------------

NODE_COLUMNS: Final[set[str]] = {"id", "label", "type"}
EDGE_COLUMNS: Final[set[str]] = {"source", "target", "relation"}


def validate_file_exists(path: Path) -> None:
    """Raise an error if a required CSV file does not exist.

    Args:
        path: Path to the CSV file.

    Raises:
        FileNotFoundError: If the file is missing.
    """
    if not path.is_file():
        raise FileNotFoundError(f"Required file not found: {path}")


def validate_columns(
    dataframe: pd.DataFrame,
    required_columns: set[str],
    filename: str,
) -> None:
    """Validate that a DataFrame contains the required columns.

    Args:
        dataframe: DataFrame to validate.
        required_columns: Expected column names.
        filename: Name of the source file (used in error messages).

    Raises:
        ValueError: If required columns are missing.
    """
    missing = required_columns.difference(dataframe.columns)

    if missing:
        missing_str = ", ".join(sorted(missing))
        raise ValueError(
            f"{filename} is missing required columns: {missing_str}"
        )


def load_nodes(path: Path = NODES_FILE) -> pd.DataFrame:
    """Load and validate node definitions.

    Args:
        path: Path to nodes.csv.

    Returns:
        DataFrame containing validated node data.
    """
    validate_file_exists(path)

    nodes = pd.read_csv(path)
    validate_columns(nodes, NODE_COLUMNS, path.name)

    return nodes


def load_edges(path: Path = EDGES_FILE) -> pd.DataFrame:
    """Load and validate edge definitions.

    Args:
        path: Path to edges.csv.

    Returns:
        DataFrame containing validated edge data.
    """
    validate_file_exists(path)

    edges = pd.read_csv(path)
    validate_columns(edges, EDGE_COLUMNS, path.name)

    return edges


def build_graph(
    nodes: pd.DataFrame,
    edges: pd.DataFrame,
) -> nx.MultiDiGraph:
    """Build a directed multigraph from node and edge tables.

    Args:
        nodes: Node definitions.
        edges: Edge definitions.

    Returns:
        A populated NetworkX MultiDiGraph.
    """
    graph = nx.MultiDiGraph()

    for row in nodes.itertuples(index=False):
        graph.add_node(
            row.id,
            label=row.label,
            type=row.type,
        )

    for row in edges.itertuples(index=False):
        graph.add_edge(
            row.source,
            row.target,
            relation=row.relation,
        )

    return graph


def export_graph(
    graph: nx.MultiDiGraph,
    output_dir: Path = OUTPUT_DIR,
) -> None:
    """Export the graph to GraphML and GEXF.

    Args:
        graph: Graph to export.
        output_dir: Destination directory.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    nx.write_graphml(graph, output_dir / "graph.graphml")
    nx.write_gexf(graph, output_dir / "graph.gexf")


def print_summary(
    graph: nx.MultiDiGraph,
    nodes: pd.DataFrame,
    edges: pd.DataFrame,
) -> None:
    """Print a summary of the generated knowledge graph.

    Args:
        graph: Built graph.
        nodes: Node table.
        edges: Edge table.
    """
    node_types = nodes["type"].nunique()
    relation_types = edges["relation"].nunique()

    print("\nFrontier AI Governance Knowledge Graph")
    print("-" * 45)
    print(f"Nodes           : {graph.number_of_nodes():,}")
    print(f"Edges           : {graph.number_of_edges():,}")
    print(f"Node types      : {node_types:,}")
    print(f"Relation types  : {relation_types:,}")
    print(f"GraphML         : {GRAPHML_FILE}")
    print(f"GEXF            : {GEXF_FILE}")


def main() -> None:
    """Application entry point."""
    nodes = load_nodes()
    edges = load_edges()

    graph = build_graph(nodes, edges)

    export_graph(graph)
    print_summary(graph, nodes, edges)


if __name__ == "__main__":
    main()
