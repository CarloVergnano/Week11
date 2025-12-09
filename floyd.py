import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
             # (nodo u, nodo v, ATTRIBUTO=weight)
lista_nodi = [(0, 1, 5), (1, 2, 2), (2, 3, -3), (1, 3, 10), (3, 2, 8)]
G.add_weighted_edges_from(lista_nodi)

fw = nx.floyd_warshall(G, weight="weight") #indica quale informazione dell'arco vogliamo utilizzare oer il percorso minimo, sopra avevo il peso quindi scrivo osì
for a, b in fw.items(): #tiro fuori gli item e stampo quali sono in ordine raggiungbile da ciascun nodo e il peso. Da 0 per arrivare ad 1 peso 5.
    print(a)
    print(dict(b))


pos = nx.planar_layout(G) #da creare di default
nx.draw(G, pos, with_labels=True) #da creare di default, se voglio aggiungere i labels devo scrivere anche l'ultima roba
labels = nx.get_edge_attributes(G, "weight") #calcolo le etichette, ottengo gli attributi che sarebbero i pesi tra i due numeri
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) #qua aggiungo i labels  così si vedra la lunghezza delle distanze

plt.savefig("plot") #creare una figura o mostrare il risultato
plt.show()# fa vedere la figura