#!/usr/bin/env bash
set -euo pipefail

if [ -f graph/node_types.csv ]; then
    mv graph/node_types.csv data/ontology/
fi

if [ -f graph/relation_types.csv ]; then
    mv graph/relation_types.csv data/ontology/
fi

echo "Ontology migrated."
