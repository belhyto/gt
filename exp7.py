import numpy as np
from scipy.optimize import linprog

def zero_sum_game_solver(payoff_matrix):
    num_strategies = len(payoff_matrix)

    # Convert to linear programming form
    c = [-1] + [0] * num_strategies  # Maximize v
    A = np.hstack((-np.ones((num_strategies, 1)), payoff_matrix))
    b = np.zeros(num_strategies)
    A_eq = [[0] + [1] * num_strategies]
    b_eq = [1]
    bounds = [(None, None)] + [(0, 1)] * num_strategies

    # Solve the linear program for Player 1
    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if res.success:
        value = 1 / res.x[0]
        strategy = res.x[1:] * value
        return value, strategy
    else:
        return None, None

# Example Payoff Matrix (Row Player)
payoff_matrix = np.array([[3, -1], [5, 2]])

value, strategy = zero_sum_game_solver(payoff_matrix)
if strategy is not None:
    print("Game Value:", round(value, 2))
    print("Optimal Mixed Strategy for Player 1:", np.round(strategy, 2))
else:
    print("No optimal strategy found.")
