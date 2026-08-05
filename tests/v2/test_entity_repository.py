from pathlib import Path

from frontier_kg.repositories.entities import EntityRepository
from frontier_kg.repositories.ontology import OntologyRepository


def test_load_entities():

    ontology = OntologyRepository(
        Path("data/ontology")
    )

    ontology.load()

    repository = EntityRepository(
        Path("data/entities"),
        ontology,
    )

    repository.load()

    assert repository.has("anthropic")
    assert repository.has("openai")
    assert repository.has("claude_opus_4")

    entity = repository.get("anthropic")

    assert entity.label == "Anthropic"

    assert len(repository.entities) > 0
