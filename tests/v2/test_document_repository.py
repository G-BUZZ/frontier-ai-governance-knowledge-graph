from pathlib import Path

from frontier_kg.repositories.documents import DocumentRepository


def test_load_documents():

    repository = DocumentRepository(
        Path("data/documents")
    )

    repository.load()

    assert repository.has("anthropic_rsp")

    document = repository.get("anthropic_rsp")

    assert document.title == "Responsible Scaling Policy"

    assert document.publisher == "Anthropic"

    assert len(repository.documents) > 0
