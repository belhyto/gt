import numpy as np

def analyze_game(matrix):
    """Analyze 2x2 matrix game for saddle points and mixed strategies"""
    # Saddle point detection
    saddle_points = []
    for i in range(2):
        row_min = min(matrix[i])
        for j in range(2):
            col_max = max(matrix[:,j])
            if matrix[i][j] == row_min and matrix[i][j] == col_max:
                saddle_points.append(matrix[i][j])

    # Mixed strategy calculation (if no saddle point)
    if not saddle_points:
        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
        denominator = (a + d) - (b + c)

        if denominator != 0:
            p = (d - c) / denominator
            q = (d - b) / denominator
        else:  # Handle zero denominator case
            p, q = 0.5, 0.5

        return {
            'saddle_point': None,
            'row_strategy': [p, 1-p],
            'col_strategy': [q, 1-q]
        }

    return {'saddle_point': saddle_points[0]}

# Example usage
game_matrix = np.array([[3, 1], [2, 4]])
result = analyze_game(game_matrix)

if result['saddle_point']:
    print(f"Saddle point found: {result['saddle_point']}")
else:
    print(f"Mixed strategies:\nRow: {result['row_strategy']}\nColumn: {result['col_strategy']}")
