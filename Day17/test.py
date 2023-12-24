def iterate_diagonally(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    for s in range(rows + cols - 1):
        for row in range(s + 1):
            col = s - row
            if row < rows and col < cols:
                yield (row, col)

# Example usage
grid = [[0]*4 for _ in range(4)]  # Replace this with your actual 2D array
for row, col in iterate_diagonally(grid):
    print(row, col)
