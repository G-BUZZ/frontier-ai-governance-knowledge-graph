from pathlib import Path

from frontier_kg.builders import KnowledgeGraphBuilder


def test_build_graph():

    builder = KnowledgeGraphBuilder(Path("data"))

    graph = builder.build()

    assert len(graph.ontology_classes) > 0
    assert len(graph.relation_types) > 0
    assert len(graph.documents) > 0
    assert len(graph.entities) > 0
    assert len(graph.assertions) == 4
