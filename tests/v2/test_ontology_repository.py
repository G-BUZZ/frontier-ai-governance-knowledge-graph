from pathlib import Path

from frontier_kg.repositories.ontology import OntologyRepository


def test_load_ontology():

    repository = OntologyRepository(
        Path("data/ontology")
    )

    repository.load()

    assert repository.has_class("organization")
    assert repository.has_class("frontier_model")
    assert repository.has_class("publication")

    assert repository.has_relation("develops")
    assert repository.has_relation("publishes")
    assert repository.has_relation("references")

    assert len(repository.classes) > 0
    assert len(repository.relations) > 0
