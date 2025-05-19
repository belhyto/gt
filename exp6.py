import numpy as np
import nashpy as nash

def find_saddle_point(matrix):
    """Check for saddle points in a 2x2 matrix."""
    row_mins = np.min(matrix, axis=1)
    col_maxes = np.max(matrix, axis=0)
    saddle_points = matrix[(matrix == row_mins[:, None]) & (matrix == col_maxes[None, :])]
    return saddle_points[0] if saddle_points.size > 0 else None

def analyze_bayesian_game():
    # Beliefs (type probabilities)
    beliefs = {"Player 1": [0.5, 0.5], "Player 2": [0.5, 0.5]}

    # Payoffs for each (type1, type2, strategy1, strategy2)
    payoffs = {
        (0, 0, 0, 0): (3, 2), (0, 0, 0, 1): (1, 4), (0, 0, 1, 0): (5, 1), (0, 0, 1, 1): (2, 3),
        (0, 1, 0, 0): (4, 3), (0, 1, 0, 1): (2, 2), (0, 1, 1, 0): (1, 5), (0, 1, 1, 1): (3, 4),
        (1, 0, 0, 0): (2, 1), (1, 0, 0, 1): (3, 5), (1, 0, 1, 0): (4, 2), (1, 0, 1, 1): (1, 3),
        (1, 1, 0, 0): (3, 4), (1, 1, 0, 1): (5, 2), (1, 1, 1, 0): (1, 3), (1, 1, 1, 1): (2, 1),
    }

    # Construct expected payoff matrices
    p1_payoff = np.zeros((2, 2))  # Player 1's expected payoffs
    p2_payoff = np.zeros((2, 2))  # Player 2's expected payoffs
    for (t1, t2, s1, s2), (p1, p2) in payoffs.items():
        prob = beliefs["Player 1"][t2] * beliefs["Player 2"][t1]  # Joint type probability
        p1_payoff[s1, s2] += prob * p1
        p2_payoff[s1, s2] += prob * p2

    # Check for saddle point
    saddle = find_saddle_point(p1_payoff)  # Check Player 1's matrix (or p2_payoff for Player 2)
    if saddle is not None:
        print(f"Saddle point found: {saddle}")
        return

    # Create Nashpy game
    game = nash.Game(p1_payoff, p2_payoff)

    # Compute Nash equilibria
    print("\nBayesian Nash Equilibria:")
    equilibria = game.support_enumeration()
    for eq in equilibria:
        print(f"Player 1: {eq[0]}, Player 2: {eq[1]}")

# Run the analysis
analyze_bayesian_game()
