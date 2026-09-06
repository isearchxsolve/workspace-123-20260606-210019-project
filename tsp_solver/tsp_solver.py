import networkx as nx
from itertools import combinations
from operator import itemgetter

def solve(graph):
    # Get all possible routes
    routes = list(combinations(graph.nodes, len(graph.nodes)))

    # Initialize minimum distance and best route
    min_distance = float('inf')
    best_route = None

    # Iterate over all routes
    for route in routes:
        # Calculate the total distance of the route
        distance = 0
        for i in range(len(route) - 1):
            distance += graph.get_edge_data(route[i], route[i + 1])['weight']

        # Update minimum distance and best route if necessary
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route
