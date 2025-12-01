from database.DAO import DAO
import networkx as nx
from model.connessione import Connessione


class Model:
    def __init__(self):
        self._objects_list = []
        self.getObjects()
        #mi posso creare anche un dizionario di object
        self._objects_dict = {}
        for o in self._objects_list:
            self._objects_dict[o._object_id] = o
        #grafo semplice non diretto ma pesato
        self._grafo = nx.Graph()


    def getObjects(self):
        self._objects_list = DAO.readObjects()

    def buildGrafo(self):

        #nodi
        self._grafo.add_nodes_from(self._objects_list)

        #archi
        #MODO 1 (80k x 80k query SQL)
        """
        for u in self._objects_list:
            for v in self._objects_list:
                DAO.readEdges(u, v)"""

        #MODO 2 (usare una query sola per estrarre le connessioni)
        connessioni = DAO.readConnessioni(self._objects_dict)
        #leggo le connessioni dal DAO
        for c in connessioni:
            self._grafo.add_edge(c.o1, c.o2, peso = c.peso)

    def calcolaConnessa(self, id_nodo):
        nodo_sorgente = self._objects_dict[id_nodo]
        successori = nx.dfs_successors(self._grafo, nodo_sorgente)
        print(f"Successori: {len(successori)}")

        #Usando i predecessori
        predecessori = nx.dfs_predecessors(self._grafo, nodo_sorgente)
        print(f"Predecessori: {len(predecessori)}")

        # Usando l'albero
        tree = nx.dfs_tree(self._grafo, nodo_sorgente)
        print(f"Albero: {len(tree.nodes)}")
        return len(tree.nodes)




