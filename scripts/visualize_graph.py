"""Visualize the Frontier AI Governance Knowledge Graph."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

PROJECT_ROOT = Path(__file__).resolve().parent.parent

GRAPH_FILE = PROJECT_ROOT / "outputs" / "graph.graphml"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "figures"
OUTPUT_FILE = OUTPUT_DIR / "knowledge_graph.png"


def main() -> None:
    """Generate a PNG visualization of the knowledge graph."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    graph = nx.read_graphml(GRAPH_FILE)

    colors = {
        "Frontier Model": "#1f77b4",
        "Governance Framework": "#ff7f0e",
        "Benchmark": "#2ca02c",
        "Risk Domain": "#d62728",
        "Organization": "#9467bd",
        "Capability": "#8c564b",
    }

    node_colors = [
        colors.get(graph.nodes[node].get("type", ""), "#7f7f7f")
        for node in graph.nodes
    ]

    pagerank = nx.pagerank(graph)

    node_sizes = [
        8000 * pagerank[node] + 300
        for node in graph.nodes
    ]

    pos = nx.spring_layout(
        graph,
        seed=42,
        k=1.2,
    )

    plt.figure(figsize=(14, 10))

    nx.draw_networkx_edges(
        graph,
        pos,
        alpha=0.4,
        arrows=True,
        arrowsize=18,
    )

    nx.draw_networkx_nodes(
        graph,
        pos,
        node_color=node_colors,
        node_size=node_sizes,
    )

    labels = {
        node: graph.nodes[node].get("label", node)
        for node in graph.nodes
    }

    nx.draw_networkx_labels(
        graph,
        pos,
        labels,
        font_size=8,
    )

    plt.axis("off")
    plt.tight_layout()

    plt.savefig(
        OUTPUT_FILE,
        dpi=300,
        bbox_inches="tight",
    )

    print(f"Figure exported to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
