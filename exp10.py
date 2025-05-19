import itertools
import math  # Use standard math instead of deprecated np.math

def shapley_value(players, coalition_values):
    n = len(players)
    shapley_values = {player: 0 for player in players}

    for player in players:
        # Iterate through all possible coalition sizes (1 to n)
        for coalition_size in range(1, n + 1):
            # Generate all possible coalitions of current size
            for coalition in itertools.combinations(players, coalition_size):
                if player in coalition:
                    # Remove target player to get predecessor coalition
                    S = tuple(p for p in coalition if p != player)

                    # Calculate weight factor
                    s = len(S)
                    weight = (math.factorial(s) * math.factorial(n - s - 1)) / math.factorial(n)

                    # Compute marginal contribution
                    marginal = coalition_values.get(coalition, 0) - coalition_values.get(S, 0)

                    shapley_values[player] += weight * marginal
    return shapley_values

# Example usage remains the same
players = ['A', 'B', 'C']
coalition_values = {
    (): 0,
    ('A',): 1, ('B',): 2, ('C',): 3,
    ('A', 'B'): 5, ('A', 'C'): 6, ('B', 'C'): 8,
    ('A', 'B', 'C'): 10
}

shapley_vals = shapley_value(players, coalition_values)
print("Shapley Values:")
for player, value in shapley_vals.items():
    print(f"Player {player}: {round(value, 2)}")
