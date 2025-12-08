import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
             # (u, v, weight)
lista_nodi = [(0, 1, 5), (1, 2, 2), (2, 3, -3), (1, 3, 10), (3, 2, 8)]
G.add_weighted_edges_from(lista_nodi)

fw = nx.floyd_warshall(G, weight="weight")
for a, b in fw.items():
    print(a)
    print(dict(b))


pos = nx.planar_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.savefig("plot")
plt.show()