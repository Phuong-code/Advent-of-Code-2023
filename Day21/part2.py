import numpy as np

with open("Day21\input.txt", "r") as file:
    grid = [list(line) for line in file.read().split("\n")]

row_num = len(grid)
col_num = len(grid[0])

for row in range(row_num):
    for col in range(col_num):
        if grid[row][col] == "S":
            s_row = row
            s_col = col

total_step_list = [65 +131*i for i in range(3)]
X,Y=[0,1,2],[]
target = (26501365 - 65)//131
for total_step in total_step_list:
    seen = set((s_row, s_col))
    ans = set()
    queue = [(s_row, s_col, 0)]
    while queue:
        row, col, step = queue.pop(0)
        if total_step % 2 == 1:
            if step % 2 == 1:
                ans.add((row, col))
        else:
            if step % 2 == 0:
                ans.add((row, col))
        if step == total_step:
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = row + dr
            new_col = col + dc
            converted_new_row = new_row % row_num
            converted_new_col = new_col % col_num
            if (grid[converted_new_row][converted_new_col] != "#" and
                (new_row, new_col) not in seen):
                seen.add((new_row, new_col))
                queue.append((new_row, new_col, step+1))
    Y.append(len(ans))

poly = np.rint(np.polynomial.polynomial.polyfit(X,Y,2)).astype(int).tolist()
print(sum(poly[i]*target**i for i in range(3)))