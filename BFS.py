from collections import deque
from Grafo import Grafo

nodos = ['car', 'cat', 'cab', 'mat', 'bat', 'bab']
vecinos = [['cab', 'cat'], ['mat', 'bat'], ['cat', 'bab'], ['bat'], [], ['bat']]

grafo = Grafo()
grafo.create_graph(nodos, vecinos)


def bfs_tree(grafo, inicio):
    queue = deque()
    queue += [grafo.nodo[inicio]]
    while queue:
        nodo = queue.popleft()
        nodo.analizado = True
        for neighbor in nodo.vecinos:
            if not neighbor.analizado:
                queue.append(neighbor)
                neighbor.padre = nodo
                neighbor.analizado = True

bfs_tree(grafo, 'car')

for nodo_id, nodo in grafo.nodo.items():
    if nodo.padre:
        print(f"Nodo: {nodo.id}, Padre: {nodo.padre.id}")
    else:
        print(f"Nodo: {nodo.id}, Padre: None")