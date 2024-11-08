from BFS import bfs_tree, get_path
from DFS import get_deep_path
from Graph import Graph


def create_graph():
    nodes = ['car', 'cat', 'cab', 'mat', 'bat', 'bab']
    neighbors = [['cab', 'cat'], ['mat', 'bat'], ['cat', 'bab'], ['bat'], [], ['bat']]

    graph = Graph()
    graph.create_graph(nodes, neighbors)
    return graph


def main():
    print('Creatring graph...')
    graph = create_graph()

    print('******** SHORTEST PATH ********')
    start = input('Enter the start node: ')
    finish = input('Enter the finish node: ')
    bfs_tree(graph, start)
    path = get_path(graph, finish)
    print('The shortest path from {} to {} is: {}'.format(start, finish, path))

    print('\n******** DEEPEST PATH ********')
    start = input('Enter the start node: ')
    if input('Do you want to search a specific node? (y/n): ') == 'y':
        finish = input('Enter the finish node: ')
        deep_path, max_deep = get_deep_path(graph, start, finish)
        print('The deepest path from {} to {} is {}'.format(start, finish, deep_path))
    else:
        deep_path, max_deep = get_deep_path(graph, start)
        print('The deepest path in the graph is {}'.format(deep_path))

if __name__ == '__main__':
    main()