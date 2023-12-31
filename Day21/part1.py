with open("Day21\input.txt", "r") as file:
    grid = [list(line) for line in file.read().split("\n")]

row_num = len(grid)
col_num = len(grid[0])
found = False
for row in range(row_num):
    for col in range(col_num):
        if grid[row][col] == "S":
            s_row = row
            s_col = col
            found = True
            break
    if found:
        break


seen = set((s_row, s_col))
ans = set()
queue = [(s_row, s_col, 0)]

while queue:
    row, col, step = queue.pop(0)
    if step % 2 == 0:
        ans.add((row, col))
    if step == 64:
        continue
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row = row + dr
        new_col = col + dc
        if (0 <= new_row < row_num and 
            0 <= new_col < col_num and 
            grid[new_row][new_col] != "#" and
            (new_row, new_col) not in seen):
            seen.add((new_row, new_col))
            queue.append((new_row, new_col, step+1))

print(len(ans))
