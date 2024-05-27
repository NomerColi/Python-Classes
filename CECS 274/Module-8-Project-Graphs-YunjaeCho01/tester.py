from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix
import random
import copy


def test():
    """write your own tester in this function"""
    n = 4
    edges = [(0, 0), (0, 3), (3, 2), (0, 1), (0, 0), (0, 2)]
    graph_list = AdjacencyList(n)
    graph_matrix = AdjacencyMatrix(n)
    for edge in edges:
        i = edge[0]
        j = edge[1]
        graph_list.add_edge(i, j)
        graph_matrix.add_edge(i, j)
    print("Edges:", edges)
    #print("Adjacency list graph:\n", graph_list)
    print("Adjacency matrix graph:\n", graph_matrix)
    #print("Adjacency list graph in edges:\n", graph_list.in_edges(2))

    print(f"remove: {graph_matrix.remove_edge(0, 1)}")

    #print("Adjacency list graph bfs:\n", graph_list.bfs(0))
    #print("Adjacency list graph dfs:\n", graph_list.bfs(0))
    #print("Adjacency matrix graph bfs:\n", graph_matrix.bfs(0))
    #print("Adjacency matrix graph dfs:\n", graph_matrix.dfs(0))
