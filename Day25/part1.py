import networkx as nx

with open("Day25\input.txt", "r") as file:
    content = file.read().splitlines()

g = nx.Graph()

for line in content:
    left, right = line.split(":")
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))