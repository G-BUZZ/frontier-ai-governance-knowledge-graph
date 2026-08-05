# Frontier AI Governance Knowledge Graph

![CI](https://github.com/G-BUZZ/frontier-ai-governance-knowledge-graph/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An open, evidence-based knowledge graph mapping the governance ecosystem of frontier artificial intelligence.

The project models relationships between frontier AI models, evaluations, benchmarks, governance frameworks, regulations, safety measures, deployment controls, organizations, incidents, and supporting evidence.

Rather than producing subjective rankings, this repository focuses on documenting verifiable relationships supported by primary sources.

---

## Objectives

This project aims to:

- build an evidence-based knowledge graph for frontier AI governance;
- organize governance knowledge into reusable structured data;
- connect policy documents, evaluations, standards, and technical reports;
- support governance research through transparent methodology;
- enable reproducible analyses and visualizations.

---

## Research Questions

Examples include:

- Which evaluations are most frequently referenced by frontier model developers?
- Which governance frameworks recommend deployment gating?
- Which benchmarks support biological capability assessments?
- How are incident reporting mechanisms connected to safety frameworks?
- Which organizations adopt external evaluations?

---

## Design Principles

- Evidence first
- Reproducibility
- Transparency
- Neutrality
- Source traceability
- Extensibility

---

## Architecture

```text
YAML Sources
      │
      ▼
build_dataset.py
      │
      ▼
nodes.csv / edges.csv
      │
      ▼
load_graph.py
      │
      ▼
NetworkX MultiDiGraph
      │
      ├─────────────► GraphML
      │
      ├─────────────► GEXF
      │
      ▼
Analysis
      │
      ▼
Visualizations
```

---

## Repository Structure

```text
.
├── data/
│   ├── raw/
│   ├── processed/
│   └── sources/
│
├── graph/
│
├── outputs/
│   ├── figures/
│   ├── reports/
│   ├── tables/
│   └── json/
│
├── scripts/
├── tests/
│
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Data Sources

Examples include:

- Frontier model system cards
- Technical reports
- Government publications
- AI safety frameworks
- International standards
- Academic literature
- Benchmark documentation
- Incident databases

Every relationship in the graph is intended to be traceable to publicly available evidence.

---

## Generated Artifacts

The pipeline automatically produces:

- CSV datasets
- GraphML
- GEXF
- Network statistics
- Markdown reports
- Figures
- JSON summaries

---

## Quick Start

Install dependencies

```bash
pip install -r requirements.txt
```

Build the dataset

```bash
python scripts/build_dataset.py
```

Build the graph

```bash
python scripts/load_graph.py
```

Analyze the graph

```bash
python scripts/analyze_graph.py
```

Generate visualizations

```bash
python scripts/visualize_graph.py
```

Run automated tests

```bash
pytest
```

Run static analysis

```bash
ruff check .
```

---

## Current Dataset

Current entities include:

- Organizations
- Frontier AI Models
- Governance Frameworks
- Benchmarks
- Risk Domains
- Regulations

The dataset is continuously expanded using evidence from public sources.

---

## Roadmap

- Expand entity coverage
- Expand relationship taxonomy
- Improve graph validation
- Add additional data importers
- Improve visualization
- Neo4j support
- Interactive dashboard

---

## Current Status

The repository currently includes:

- reproducible dataset pipeline
- automated validation
- GitHub Actions CI
- automated testing
- NetworkX analysis
- GraphML/GEXF export
- YAML-based knowledge representation

Development is active and the knowledge graph is under continuous expansion.

---

## License

MIT License
