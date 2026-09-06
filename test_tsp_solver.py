import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
from tsp_solver import tsp_solver

def test_tsp_solver():
    distances = np.array([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
    path = tsp_solver(distances.tolist())
    # The optimal solution for this instance is [0, 1, 3, 2, 0]
    assert path == [0, 1, 3, 2, 0]

if __name__ == '__main__':
    test_tsp_solver()