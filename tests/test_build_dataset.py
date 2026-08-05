from pathlib import Path

import yaml


def test_anthropic_yaml_exists():
    assert Path("data/sources/anthropic.yaml").exists()


def test_anthropic_yaml_schema():
    path = Path("data/sources/anthropic.yaml")

    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)

    assert "nodes" in data
    assert "edges" in data

    assert isinstance(data["nodes"], list)
    assert isinstance(data["edges"], list)


def test_every_node_has_required_fields():
    path = Path("data/sources/anthropic.yaml")

    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)

    for node in data["nodes"]:
        assert "id" in node
        assert "label" in node
        assert "type" in node
