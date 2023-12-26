with open("Day18\input.txt", "r") as file:
    instructions = [tuple(line[0:4].strip().split(" ")) for line in file.read().split("\n")]

row_nums = col_nums = 801
# row_nums = col_nums = 51 # for input-example.txt
cur_row = (row_nums-1) //2
cur_col = (row_nums-1) //2
lava_grid = [["." for i in range(col_nums)] for j in range(row_nums)]
dict = {"R" : (0, 1),
        "L" : (0, -1),
        "U" : (-1, 0),
        "D" : (1, 0)}
seen = set()

for ins in instructions:
    dir = ins[0]
    meters = int(ins[1])
    for meter in range(meters):
        dr = dict[dir][0]
        dc = dict[dir][1]
        cur_row += dr
        cur_col += dc
        lava_grid[cur_row][cur_col] = "#"
        seen.add((cur_row, cur_col))

for row in range(row_nums):
    for col in range(col_nums):
        if (row, col) in seen:
            continue
        else:
            has_up = False
            has_down = False
            count = 0
            for left in range(col):
                if (row , left) in seen:
                    if (row-1, left) in seen:
                        has_up = True
                    if (row+1, left) in seen:
                        has_down = True
                    if has_up and has_down:
                        count += 1
                else:
                    has_up = False
                    has_down = False
            if count % 2 == 1:
                lava_grid[row][col] = "#"

result = 0
for row in range(row_nums):
    for col in range(col_nums):
        if lava_grid[row][col] == "#":
            result += 1
print(result)

