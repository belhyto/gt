import nashpy as nash
import numpy as np

# Define the payoff matrices for two players
A = np.array([[-1, -3], [0, -2]])  # Player 1's payoffs
B = np.array([[-1, 0], [-3, -2]])  # Player 2's payoffs

# Create the game
game = nash.Game(A, B)

# Compute Nash Equilibria
equilibria = list(game.support_enumeration())

print("Nash Equilibria:", equilibria)
