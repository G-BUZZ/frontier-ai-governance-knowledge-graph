from pathlib import Path

from frontier_kg.repositories.assertions import AssertionRepository
from frontier_kg.repositories.documents import DocumentRepository
from frontier_kg.repositories.entities import EntityRepository
from frontier_kg.repositories.ontology import OntologyRepository


def test_load_assertions():

    ontology = OntologyRepository(Path("data/ontology"))
    ontology.load()

    documents = DocumentRepository(Path("data/documents"))
    documents.load()

    entities = EntityRepository(
        Path("data/entities"),
        ontology,
    )
    entities.load()

    repository = AssertionRepository(
        Path("data/assertions"),
        entities,
        documents,
        ontology,
    )

    repository.load()

    assert len(repository.assertions) == 4

    first = repository.assertions[0]

    assert first.id == "a001"
    assert first.subject == "anthropic"
    assert first.predicate == "publishes"
    assert first.object == "anthropic_rsp"

    assert first.provenance.document == "anthropic_rsp"
    assert first.provenance.confidence == 1.0
