import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
from tsp_solver import tsp_solver

import unittest

class TestTSPSolver(unittest.TestCase):
    def test_solve(self):
        graph = nx.Graph()
        graph.add_edge(0, 1, weight=1)
        graph.add_edge(0, 2, weight=3)
        graph.add_edge(1, 2, weight=2)
        self.assertEqual(tsp_solver.solve(graph), (0, 1, 2))

if __name__ == '__main__':
    unittest.main()
