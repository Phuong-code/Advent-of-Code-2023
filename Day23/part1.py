with open("Day23\input.txt", "r") as file:
    grid = [list(line) for line in file.read().split("\n")]

row_num = len(grid)
col_num = len(grid[0])

for col in range(col_num):
    if grid[0][col]== ".":
        s_row = 0
        s_col = col
        break

for col in range(col_num):
    if grid[row_num-1][col]== ".":
        e_row = row_num-1
        e_col = col
        break

dict = {"^": [(-1, 0)],
        ">": [(0, 1)],
        "v": [(1, 0)],
        "<": [(0, -1)],
        ".": [(1, 0), (0, 1), (0, -1), (-1, 0)]}

seen = {(s_row, s_col)}
queue = [(s_row, s_col, 0)]

max_step = 0
while queue:
    row, col, step = queue.pop()
    if row == e_row and col == e_col:
        max_step = max(step, max_step)
    for dr, dc in dict[grid[row][col]]:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < row_num and 0 <= new_col < col_num and (new_row, new_col) not in seen and grid[new_row][new_col] != "#":
            queue.append((new_row, new_col, step+1))
    seen.clear()
    seen.add((row, col))

print(max_step)