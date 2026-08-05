"""Analyze the Frontier AI Governance Knowledge Graph.

Loads the exported GraphML file, computes network metrics, exports analysis
tables, and prints a concise summary.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

import networkx as nx
import pandas as pd

# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent

GRAPH_FILE: Final[Path] = PROJECT_ROOT / "outputs" / "graph.graphml"
TABLES_DIR: Final[Path] = PROJECT_ROOT / "outputs" / "tables"

NODE_METRICS_FILE: Final[Path] = TABLES_DIR / "node_metrics.csv"
TOP_NODES_FILE: Final[Path] = TABLES_DIR / "top_central_nodes.csv"

TOP_N: Final[int] = 20


def load_graph(path: Path = GRAPH_FILE) -> nx.MultiDiGraph:
    """Load a GraphML graph."""

    if not path.exists():
        raise FileNotFoundError(f"Graph not found: {path}")

    graph = nx.read_graphml(path)

    if not isinstance(graph, nx.MultiDiGraph):
        graph = nx.MultiDiGraph(graph)

    return graph


def compute_metrics(graph: nx.MultiDiGraph) -> pd.DataFrame:
    """Compute node-level graph metrics."""

    pagerank = nx.pagerank(graph)
    degree = nx.degree_centrality(graph)
    betweenness = nx.betweenness_centrality(graph)

    records = []

    for node, attrs in graph.nodes(data=True):
        records.append(
            {
                "id": node,
                "label": attrs.get("label", ""),
                "type": attrs.get("type", ""),
                "in_degree": graph.in_degree(node),
                "out_degree": graph.out_degree(node),
                "degree_centrality": degree[node],
                "betweenness": betweenness[node],
                "pagerank": pagerank[node],
            }
        )

    return (
        pd.DataFrame(records)
        .sort_values("pagerank", ascending=False)
        .reset_index(drop=True)
    )


def export_tables(metrics: pd.DataFrame) -> None:
    """Export CSV analysis tables."""

    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    metrics.to_csv(NODE_METRICS_FILE, index=False)

    metrics.head(TOP_N).to_csv(
        TOP_NODES_FILE,
        index=False,
    )


def print_summary(graph: nx.MultiDiGraph, metrics: pd.DataFrame) -> None:
    """Print graph analysis summary."""

    print("\nKnowledge Graph Analysis")
    print("-" * 45)

    print(f"Nodes                 : {graph.number_of_nodes():,}")
    print(f"Edges                 : {graph.number_of_edges():,}")
    print(f"Density               : {nx.density(graph):.4f}")

    print(
        f"Weak components       : "
        f"{nx.number_weakly_connected_components(graph)}"
    )

    print(
        f"Average in-degree     : "
        f"{metrics['in_degree'].mean():.2f}"
    )

    print(
        f"Average out-degree    : "
        f"{metrics['out_degree'].mean():.2f}"
    )

    print("\nTop PageRank nodes")

    top = metrics.head(10)

    for i, row in enumerate(top.itertuples(index=False), start=1):
        print(
            f"{i:>2}. "
            f"{row.label} "
            f"({row.type}) "
            f"- {row.pagerank:.4f}"
        )

    print(f"\nCSV exported to: {NODE_METRICS_FILE}")
    print(f"CSV exported to: {TOP_NODES_FILE}")


def main() -> None:
    """Application entry point."""

    graph = load_graph()

    metrics = compute_metrics(graph)

    export_tables(metrics)

    print_summary(graph, metrics)


if __name__ == "__main__":
    main()
