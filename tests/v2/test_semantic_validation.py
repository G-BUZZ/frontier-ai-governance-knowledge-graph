from pathlib import Path

from frontier_kg.builders import KnowledgeGraphBuilder
from frontier_kg.validation.semantic import SemanticValidator


def test_semantic_validation():

    builder = KnowledgeGraphBuilder(
        Path("data")
    )

    graph = builder.build()

    validator = SemanticValidator()

    result = validator.validate(graph)

    assert result.valid

    assert result.errors == []
