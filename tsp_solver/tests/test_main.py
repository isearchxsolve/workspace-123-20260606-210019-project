import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from tsp_solver.main import solve_tsp

class TestMain(unittest.TestCase):
    def test_solve_tsp(self):
        num_nodes = 5
        num_edges = 10
        graph = unittest.mock.Mock(spec=dict)
        graph.number_of_nodes.return_value = num_nodes
        graph.add_edge.return_value = None
        graph.__getitem__.return_value = unittest.mock.Mock(spec=dict)
        graph.__getitem__.return_value.__getitem__.return_value = 1.0

        row_ind, col_ind = solve_tsp(graph)
        self.assertEqual(len(row_ind), num_nodes)
        self.assertEqual(len(col_ind), num_nodes)

if __name__ == '__main__':
    unittest.main()