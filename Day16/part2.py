def count_tile(dicrection, row_po,column_po):
    global grid
    global count_grid
    while True:
        if (row_po < 0 or 
            row_po >= len(grid) or 
            column_po < 0 or 
            column_po >= len(grid[0]) or
            (dicrection in count_grid[row_po][column_po])):
            return
        current_tile = grid[row_po][column_po]
        count_grid[row_po][column_po] += dicrection
        if dicrection == "R":
            if current_tile in ".-":
                dicrection = "R"
                column_po += 1
            elif current_tile == "/":
                dicrection = "U"
                row_po -= 1
            elif current_tile == "\\":
                dicrection = "D"
                row_po += 1
            elif current_tile == "|":
                count_tile("U", row_po-1 ,column_po)
                count_tile("D", row_po+1 ,column_po)
        elif dicrection == "D":
            if current_tile in ".|":
                dicrection = "D"
                row_po += 1
            elif current_tile == "/":
                dicrection = "L"
                column_po -= 1
            elif current_tile == "\\":
                dicrection = "R"
                column_po += 1
            elif current_tile == "-":
                count_tile("L", row_po ,column_po-1)
                count_tile("R", row_po ,column_po+1)
        elif dicrection == "L":
            if current_tile in ".-":
                dicrection = "L"
                column_po -= 1
            elif current_tile == "/":
                dicrection = "D"
                row_po += 1
            elif current_tile == "\\":
                dicrection = "U"
                row_po -= 1
            elif current_tile == "|":
                count_tile("U", row_po-1 ,column_po)
                count_tile("D", row_po+1 ,column_po)
        elif dicrection == "U":
            if current_tile in ".|":
                dicrection = "U"
                row_po -= 1
            elif current_tile == "/":
                dicrection = "R"
                column_po += 1
            elif current_tile == "\\":
                dicrection = "L"
                column_po -= 1
            elif current_tile == "-":
                count_tile("R", row_po ,column_po+1)
                count_tile("L", row_po ,column_po-1)

file = open("Day16\input.txt","r")
grid = file.read().split("\n")
file.close()

for i in range(len(grid)):
    grid[i] = list(grid[i])

row_numbers = len(grid)
column_numbers = len(grid[0])
max_result = 0
# def check_all_config(dicrection, row_start, column_start, count_grid):
for column in range(column_numbers):
    count_grid = [["." for _ in range(row_numbers)] for _ in range(column_numbers)]
    count_tile("D", 0, column)

    result = 0
    for row in range(row_numbers):
        for column in range(column_numbers):
            if count_grid[row][column] != ".":
                result += 1
    max_result = max(max_result, result)

for column in range(column_numbers):
    count_grid = [["." for _ in range(row_numbers)] for _ in range(column_numbers)]
    count_tile("U", row_numbers-1, column)

    result = 0
    for row in range(row_numbers):
        for column in range(column_numbers):
            if count_grid[row][column] != ".":
                result += 1
    max_result = max(max_result, result)

for row in range(row_numbers):
    count_grid = [["." for _ in range(row_numbers)] for _ in range(column_numbers)]
    count_tile("R", row, 0)

    result = 0
    for row in range(row_numbers):
        for column in range(column_numbers):
            if count_grid[row][column] != ".":
                result += 1
    max_result = max(max_result, result)

for row in range(row_numbers):
    count_grid = [["." for _ in range(row_numbers)] for _ in range(column_numbers)]
    count_tile("R", row, column_numbers-1)

    result = 0
    for row in range(row_numbers):
        for column in range(column_numbers):
            if count_grid[row][column] != ".":
                result += 1
    max_result = max(max_result, result)
print(max_result)
    

