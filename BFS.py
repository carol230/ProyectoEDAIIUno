from collections import deque
from Graph import Graph

nodes = ['car', 'cat', 'cab', 'mat', 'bat', 'bab']
neighbors = [['cab', 'cat'], ['mat', 'bat'], ['cat', 'bab'], ['bat'], [], ['bat']]

graph = Graph()
graph.create_graph(nodes, neighbors)


def bfs_tree(graph: Graph, start):
    queue = deque()
    queue += [graph.nodes[start]]
    while queue:
        node = queue.popleft()
        node.is_analized = True
        for neighbor in node.neighbors:
            if not neighbor.is_analized:
                queue.append(neighbor)
                neighbor.parent = node
                neighbor.is_analized = True

def get_path(graph, search_node):
    path = []
    node = graph.nodes.get(search_node)

    if node is None:
        print("El nodo buscado no existe en el graph.")
        return
    while node is not None:
        path.append(node.id)
        node = node.parent
    path.reverse()
    print('El path al nodo es {}'.format(path))


bfs_tree(graph, 'car')
get_path(graph, 'bat')