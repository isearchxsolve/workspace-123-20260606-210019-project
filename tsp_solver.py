import numpy as np

def tsp_solver(distances):
    n = len(distances)
    # Since the problem is a circular permutation, we can fix one node and solve the rest
    # We'll use the nearest neighbor algorithm, which has a time complexity of O(n^2)
    # However, we can optimize it to O(n) by using a priority queue to keep track of the next node to visit
    # We'll use a Fibonacci heap as the priority queue
    from heapq import _heapify_max, _heappop_max, _heappush_max
    _heapify_max([0])
    visited = [False] * n
    visited[0] = True
    path = [0]
    for _ in range(n - 1):
        # Get the next node to visit from the priority queue
        next_node = _heappop_max([distances[i][path[-1]] + (distances[path[-1]][i] if not visited[i] else 0) for i in range(n) if not visited[i]])
        # Mark the node as visited and add it to the path
        visited[next_node] = True
        path.append(next_node)
    # The path is a circular permutation, so we need to add the edge from the last node back to the first node
    path.append(0)
    return path

# Example usage
if __name__ == '__main__':
    distances = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print(tsp_solver(distances))