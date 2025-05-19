
import nashpy as nash
import numpy as np

# Define the payoff matrices for Player 1 and Player 2
A = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])  # Player 1
B = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])  # Player 2

# Create the game
game = nash.Game(A, B)

# Compute Nash Equilibria using support enumeration
equilibria = list(game.support_enumeration())

# Print the results
for eq in equilibria:
    print("Mixed Strategy Nash Equilibrium:")
    print(f"Player 1: {eq[0]}")
    print(f"Player 2: {eq[1]}")
