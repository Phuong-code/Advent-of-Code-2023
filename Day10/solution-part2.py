dict = {
    "|":["N", "S"],
    "-":["E", "W"],
    "L":["N", "E"],
    "J":["N", "W"],
    "7":["W", "S"],
    "F":["S", "E"]
}

def get_map_index(grid, row, column, dicrection, map_index):
    while grid[row][column] != "S":
        if dicrection == "N":
            row -= 1
            dicrection = "S"
        elif dicrection == "W":
            column -= 1
            dicrection = "E"
        elif dicrection == "S":
            row += 1
            dicrection = "N"
        elif dicrection == "E":
            column += 1
            dicrection = "W"
        next = grid[row][column]
        if next == "S":
            map_index.add((row, column))
            return map_index
        for val in dict[next]:
            if val != dicrection:
                dicrection = val
                map_index.add((row, column))
                break

file = open('Day10\input.txt','r')
content = file.read().split("\n")
file.close()

s_row = 0
s_column = 0

grid =[[0 for _ in range(len(content[0]))] for _ in range(len(content))]
for row in range(len(content)):
    for column in range(len(content[0])):
        grid[row][column] = content[row][column]
        if content[row][column] == "S":
            s_row = row
            s_column = column

map_index = set()
map_index.add((s_row+1,s_column))
map_index = get_map_index(grid, s_row+1, s_column, "S", map_index)

grid[s_row][s_column] = "|"

def count_invs(i, j):
    # Everything up to (but not including) j in line i
    line = grid[i]
    count = 0
    for k in range(j):
        if not (i, k) in map_index:
            continue
        count += line[k] in {"J", "L", "|"}

    return count


ans = 0
for i, line in enumerate(grid):
    for j in range(len(grid[0])):
        if not (i, j) in map_index:
            invs = count_invs(i, j)
            if invs % 2 == 1:
                ans += 1

print(ans)