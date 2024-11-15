from BFS import bfs_tree, get_path
from DFS import get_deep_path
from Graph import Graph


def create_graph():
    nodes = ['Riocentro', 'TroleBus-Laures', 'Ecovia-Riococa', 'Alborada-Shyris y Tomas de Berlanga', 'Metro-Jipijapa', 'Ecovia-Colegio24Mayo', 'Alborada-ShyrisYNacionesUnidas', 'Metro-Inaquito', 'Metro-LaCarolina', 'Ecovia-CasaCultura', 'Alborada-12OctubreTarqui', 'Metro-LaPradera', 'Metro-ElEjido', 'Ecovia-MarinCentral', 'Metro-UCE', 'Metro-Alameda', 'Metro-SanFrancisco','CentroHistorico']
    

    neighbors = [['TroleBus-Laures', 'Ecovia-Riococa', 'Alborada-Shyris y Tomas de Berlanga'], ['Metro-Jipijapa', 'Ecovia-Riococa'], ['TroleBus-Laures', 'Ecovia-Colegio24Mayo'], ['Alborada-ShyrisYNacionesUnidas', 'Metro-Jipijapa'], ['Metro-Inaquito', 'Alborada-Shyris y Tomas de Berlanga'], ['Metro-LaCarolina', 'Ecovia-CasaCultura'], ['Metro-Inaquito', 'Alborada-12OctubreTarqui'], ['Metro-LaCarolina', 'Alborada-ShyrisYNacionesUnidas'], ['Metro-LaPradera'], ['Metro-ElEjido', 'Alborada-12OctubreTarqui', 'Ecovia-MarinCentral'], ['Ecovia-CasaCultura', 'Metro-ElEjido', 'Ecovia-MarinCentral'], ['Metro-UCE'], ['Metro-Alameda', 'Alborada-12OctubreTarqui', 'Ecovia-CasaCultura'], ['CentroHistorico'], ['Metro-ElEjido'], ['Metro-SanFrancisco'], ['CentroHistorico'],[]]


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