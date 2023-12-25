from heapq import heapify, heappop, heappush

with open("Day17/input.txt", "r") as file:
    grid = [list(map(int, line.strip())) for line in file if line.strip()]

queue = [(0, 0, 0, 0, 0, 0)]
seen = set()
heapify(queue)
while queue:
    heat, r, c, dr, dc, s = heappop(queue)
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print(heat)
        break

    if (r, c, dr, dc, s) in seen:
        continue

    seen.add((r, c, dr, dc, s))
    for next_dr, next_dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_r = r + next_dr
        next_c = c + next_dc
        if next_r < 0 or next_r >= len(grid) or next_c < 0 or next_c >= len(grid[0]):
            continue
        if next_dr == -dr and next_dc == -dc:
            continue
        if next_dr == dr and next_dc == dc:
            if s == 3:
                continue
            else:
                heappush(queue, (heat + grid[next_r][next_c], next_r, next_c, next_dr, next_dc, s + 1))
        else:
            heappush(queue, (heat + grid[next_r][next_c], next_r, next_c, next_dr, next_dc, 1))