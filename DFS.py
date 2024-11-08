from Graph import Graph
from Node import Node

nodes = ['car', 'cat', 'cab', 'mat', 'bat', 'bab']
neighbors = [['cab', 'cat'], ['mat', 'bat'], ['cat', 'bab'], ['bat'], [], ['bat']]

graph = Graph()
graph.create_graph(nodes, neighbors)


def get_deep_path(graph: Graph, start, finish = None):
    max_deep = 0
    deep_path = []
    path = []
    start_node = graph.nodes.get(start)

    def dfs(start_node: Node, path, finish = None):
        nonlocal max_deep, deep_path
        path.append(start_node.id)

        if len(path) > max_deep and (finish is None or path[-1] == finish):
            max_deep = len(path)
            deep_path = path[:]

        for neighbor in start_node.neighbors:
            if neighbor.id not in path and not neighbor.is_analized:
                dfs(neighbor,path, finish)

        path.pop()

    dfs(start_node, path, finish)

    return deep_path, max_deep

deep_path, max_deep = get_deep_path(graph, 'car', 'mat')

print('The deepest path is {}'.format(deep_path))