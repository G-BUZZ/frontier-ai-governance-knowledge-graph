"""
Knowledge Graph Builder.

Coordinates the loading of ontology, documents,
entities and assertions into a KnowledgeGraph.
"""

from pathlib import Path

from frontier_kg.domain.graph import KnowledgeGraph
from frontier_kg.repositories.assertions import AssertionRepository
from frontier_kg.repositories.documents import DocumentRepository
from frontier_kg.repositories.entities import EntityRepository
from frontier_kg.repositories.ontology import OntologyRepository


class KnowledgeGraphBuilder:

    def __init__(self, data_dir: Path):

        self.data_dir = Path(data_dir)

    def build(self) -> KnowledgeGraph:

        ontology = OntologyRepository(
            self.data_dir / "ontology"
        )
        ontology.load()

        documents = DocumentRepository(
            self.data_dir / "documents"
        )
        documents.load()

        entities = EntityRepository(
            self.data_dir / "entities",
            ontology,
        )
        entities.load()

        assertions = AssertionRepository(
            self.data_dir / "assertions",
            entities,
            documents,
            ontology,
        )
        assertions.load()

        return KnowledgeGraph(
            ontology_classes=ontology.classes,
            relation_types=ontology.relations,
            entities=entities.entities,
            documents=documents.documents,
            assertions=assertions.assertions,
        )
