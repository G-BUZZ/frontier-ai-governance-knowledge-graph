from pathlib import Path


def test_graphml_exists():
    assert Path("outputs/graph.graphml").exists()


def test_gexf_exists():
    assert Path("outputs/graph.gexf").exists()
