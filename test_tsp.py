import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
from tsp import solve_tsp

def test_solve_tsp():
    # Example distances matrix
    distances = np.array([[0, 10, 15, 20],
                           [10, 0, 35, 25],
                           [15, 35, 0, 30],
                           [20, 25, 30, 0]])
    expected_tour = [1, 2, 0, 3]
    assert np.array_equal(solve_tsp(distances), expected_tour)

if __name__ == '__main__':
    test_solve_tsp()
