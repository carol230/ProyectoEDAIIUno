from Arista import Arista
from Node import Node

class Graph:

    def __init__(self):
        self.nodes = {}
        self.arista = []

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    def agregar_arista(self, arista: Arista):
        self.arista.append(arista)

    def create_graph(self, id_list: list, neighbor_list: list) -> None:
        if len(id_list) == len(neighbor_list):
            for id in id_list:
                node = Node(id)
                self.add_node(node)
            for i, neighbors in enumerate(neighbor_list):
                node = self.nodes[id_list[i]]
                for neighbor in neighbors:
                    node.neighbors.append(self.nodes[neighbor])
            print('Graph created')
        else:
            print('Lists do not match in size')

    def reset_graph(self):
        for node in self.nodes.values():
            node.is_analized = False