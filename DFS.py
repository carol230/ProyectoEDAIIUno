from Grafo import Grafo

nodos = ['car', 'cat', 'cab', 'mat', 'bat', 'bab']
vecinos = [['mat','cat', 'cab'], ['mat', 'bat'], ['cat', 'bab'], ['bat'], [], ['bat']]

grafo = Grafo()
grafo.create_graph(nodos, vecinos)


def ruta_profunda(grafo: Grafo, inicio, fin = None):
    max_profundidad = 0
    ruta_profunda = []
    path = []
    nodo_inicio = grafo.nodo.get(inicio)

    def dfs(nodo_inicio, path, fin = None):
        nonlocal max_profundidad, ruta_profunda
        path.append(nodo_inicio.id)

        if len(path) > max_profundidad and (fin is None or path[-1] == fin):
            max_profundidad = len(path)
            ruta_profunda = path[:]

        for vecino in nodo_inicio.vecinos:
            if vecino.id not in path and not vecino.analizado:
                dfs(vecino,path, fin)

        path.pop()
    dfs(nodo_inicio, path, fin)

    print(max_profundidad)
    print(ruta_profunda)

ruta_profunda(grafo, 'car', 'mat')