import networkx as nx
import numpy as np
from scipy.optimize import linear_sum_assignment
from itertools import combinations

def calculate_distance(graph, node1, node2):
    return graph[node1][node2]['weight']

def solve_tsp(graph):
    num_nodes = graph.number_of_nodes()
    distances = np.zeros((num_nodes, num_nodes))

    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            distances[i, j] = calculate_distance(graph, i, j)
            distances[j, i] = distances[i, j]

    row_ind, col_ind = linear_sum_assignment(distances)
    return row_ind.tolist(), col_ind.tolist()

def generate_random_graph(num_nodes, num_edges):
    graph = nx.Graph()
    for i in range(num_nodes):
        graph.add_node(i)
    for _ in range(num_edges):
        node1, node2 = np.random.randint(0, num_nodes, 2)
        if node1 != node2:
            graph.add_edge(node1, node2, weight=np.random.rand())
    return graph

def main():
    num_nodes = 10
    num_edges = 20
    graph = generate_random_graph(num_nodes, num_edges)
    row_ind, col_ind = solve_tsp(graph)
    print('Optimal tour: ', row_ind, col_ind)

if __name__ == '__main__':
    main()