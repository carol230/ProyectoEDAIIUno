from Arista import Arista
from Nodo import Nodo

class Grafo:

    def __init__(self):
        self.nodo = {}
        self.arista = []

    def agregar_nodo(self, nodo: Nodo):
        self.nodo[nodo.id] = nodo

    def agregar_arista(self, arista: Arista):
        self.arista.append(arista)

    def create_graph(self, id_list: list, neighbor_list: list) -> None:
        if len(id_list) == len(neighbor_list):
            for id in id_list:
                nodo = Nodo(id)
                self.nodo[nodo.id] = nodo
            for i, neighbors in enumerate(neighbor_list):
                nodo = self.nodo[id_list[i]]
                for neighbor in neighbors:
                    nodo.vecinos.append(self.nodo[neighbor])
        else:
            print('Las listas no coinciden en tamaño')

    def obtener_nodo(self, id_nodo):
        return self.nodo[id_nodo]