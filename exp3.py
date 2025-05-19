import numpy as np

# Get matrix dimensions
R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))

# Input matrix entries
print("Enter the entries in a single line (separated by space): ")
entries = list(map(int, input().split()))

# Create matrix
A = np.array(entries).reshape(R, C)
print("\nMatrix:\n", A)

# Saddle point detection
row_mins = np.min(A, axis=1)  # Min of each row
col_maxes = np.max(A, axis=0)  # Max of each column
saddle_points = A[(A == row_mins[:, None]) & (A == col_maxes[None, :])]

if saddle_points.size > 0:
    print(f"\nSaddle point found: {saddle_points[0]}")
else:
    print("\nNo saddle point found")

# Mixed strategy for 2x2 matrix
if R == C == 2:
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    denom = (a + d) - (b + c)
    if denom != 0:
        p1 = (d - c) / denom
        q1 = (d - b) / denom
    else:
        p1 = q1 = 0.5
    p2 = 1 - p1
    q2 = 1 - q1
    print(f"\nMixed strategies:\np1 = {p1:.2f}, p2 = {p2:.2f}, q1 = {q1:.2f}, q2 = {q2:.2f}\n")
