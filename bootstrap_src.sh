#!/usr/bin/env bash
set -euo pipefail

mkdir -p src

touch src/__init__.py

touch src/model.py
touch src/builder.py
touch src/ontology.py
touch src/entities.py
touch src/assertions.py
touch src/provenance.py
touch src/validation.py
touch src/export.py

echo "src/ bootstrapped."
