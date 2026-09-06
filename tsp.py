import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_tsp(distances):
    return linear_sum_assignment(distances)[1]

def main():
    # Example distances matrix
    distances = np.array([[0, 10, 15, 20],
                           [10, 0, 35, 25],
                           [15, 35, 0, 30],
                           [20, 25, 30, 0]])
    tour = solve_tsp(distances)
    print('Optimal tour:', tour)

if __name__ == '__main__':
    main()
