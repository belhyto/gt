import numpy as np
import matplotlib.pyplot as plt

# Define the payoff matrix for a two-strategy game
A = np.array([[3, 0],  # Payoff when both choose strategy 1
              [5, 1]]) # Payoff when one chooses strategy 1, the other strategy 2

# Replicator dynamics function
def replicator_dynamics(x, A, timesteps=100, dt=0.01):
    """
    Simulate the evolution of strategy fractions in a population.
    x: Initial strategy distribution (e.g., [0.5, 0.5])
    A: Payoff matrix
    timesteps: Number of iterations
    dt: Step size for time evolution
    """
    x_history = [x]

    for _ in range(timesteps):
        fitness = A @ x  # Compute fitness of each strategy
        avg_fitness = np.dot(x, fitness)  # Compute average fitness
        x = x + dt * (x * (fitness - avg_fitness))  # Replicator equation
        x = np.clip(x, 0, 1)  # Ensure values remain valid
        x /= np.sum(x)  # Normalize to sum to 1
        x_history.append(x.copy())

    return np.array(x_history)

# Initial strategy distribution (50% each strategy)
x0 = np.array([0.5, 0.5])

# Simulate evolution
evolution = replicator_dynamics(x0, A, timesteps=500, dt=0.01)

# Plot the results
plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
plt.plot(evolution[:, 0], label="Strategy 1")
plt.plot(evolution[:, 1], label="Strategy 2")
plt.xlabel("Time Steps")
plt.ylabel("Strategy Frequency")
plt.title("Evolutionary Game Theory - Replicator Dynamics")
plt.legend()
plt.grid(True)  # Add grid for better visualization
plt.show()
