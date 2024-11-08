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

def obtener_ruta(grafo, buscado):
    path = []
    nodo_actual = grafo.nodo.get(buscado)

    if nodo_actual is None:
        print("El nodo buscado no existe en el grafo.")
        return

    while nodo_actual is not None:
        path.append(nodo_actual.id)
        nodo_actual = nodo_actual.padre

    path.reverse()
    print('El path al nodo es {}'.format(path))


bfs_tree(grafo, 'car')
obtener_ruta(grafo, 'bat')