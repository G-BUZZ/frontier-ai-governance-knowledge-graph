import pandas as pd
import networkx as nx

nodes = pd.read_csv("graph/nodes.csv")
edges = pd.read_csv("graph/edges.csv")

G = nx.DiGraph()

for _, row in nodes.iterrows():
    G.add_node(row["id"], label=row["label"], type=row["type"])

for _, row in edges.iterrows():
    G.add_edge(row["source"], row["target"], relation=row["relation"])

print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
nx.write_graphml(G, "outputs/graph.graphml")

print("GraphML exported to outputs/graph.graphml")
