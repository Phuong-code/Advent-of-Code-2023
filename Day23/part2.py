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

start_point = (s_row, s_col)
end_point = (e_row, e_col)

points = {start_point, end_point}
for row in range(row_num):
    for col in range(col_num):
        if grid[row][col] != "#":
            neighbor = 0
            for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                neighbor_row = row + dr
                neighbor_col = col + dc
                if 0 <= neighbor_row < row_num and 0 <= neighbor_col < col_num and grid[neighbor_row][neighbor_col] != "#":
                    neighbor += 1
            if neighbor >= 3:
                points.add((row, col))

graph ={pt : {} for pt in points}
for start_row, start_col in points:
    seen = set()
    queue = [(start_row, start_col, 0)]
    while queue:
        row, col, step = queue.pop(0)
        if (row, col) in points and (row, col) != (start_row, start_col):
            graph[(start_row, start_col)][(row, col)] = step
        else:
            for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < row_num and 0 <= new_col < col_num and (new_row, new_col) not in seen and grid[new_row][new_col] != "#":
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, step+1))

seen = set()
def dfs(pt):
    if pt == end_point:
        return 0
    max_step = -float("inf")
    seen.add(pt)
    for nx in graph[pt]:
        if nx not in seen:
            max_step = max(max_step, dfs(nx) + graph[pt][nx])
    seen.remove(pt) 
    return max_step

print(dfs(start_point))   