"""
Semantic validator.

Checks ontology consistency of the built knowledge graph.
"""

from __future__ import annotations

from frontier_kg.domain.graph import KnowledgeGraph
from frontier_kg.validation.result import ValidationResult


class SemanticValidator:

    def validate(
        self,
        graph: KnowledgeGraph,
    ) -> ValidationResult:

        result = ValidationResult()

        for assertion in graph.assertions:

            relation = graph.relation_types[
                assertion.predicate
            ]

            subject = graph.entities[
                assertion.subject
            ]

            obj = graph.entities[
                assertion.object
            ]

            if subject.type != relation.domain:

                result.add(
                    assertion.id,
                    (
                        f"Subject type '{subject.type}' "
                        f"does not match "
                        f"relation domain "
                        f"'{relation.domain}'."
                    ),
                )

            if obj.type != relation.range:

                result.add(
                    assertion.id,
                    (
                        f"Object type '{obj.type}' "
                        f"does not match "
                        f"relation range "
                        f"'{relation.range}'."
                    ),
                )

        return result
