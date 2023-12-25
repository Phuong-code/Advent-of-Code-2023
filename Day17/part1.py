def iterate_diagonally(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    for s in range(rows + cols - 1):
        for row in range(s + 1):
            col = s - row
            if row < rows and col < cols:
                yield (row, col)

def is_not_consec(row, column, direction):
    global seen
    global row_numbers
    global column_numbers
    if direction == "U":
        if row+2 < row_numbers:
            if seen[row][column] == (row+1, column) and seen[row+1][column] == (row+2,column):
                return False
        # if row+3 < row_numbers:
        #     if seen[row][column] == (row+1, column) and seen[row+1][column] == (row+2,column) and seen[row+2][column] == (row+3,column):
        #         return False
    elif direction == "D":
        if 0 <= row-3:
            if seen[row][column] == (row-1, column) and seen[row-1][column] == (row-2,column) and seen[row-2][column] == (row-3,column):
                return False
        # if 0 <= row-2:
        #     if seen[row][column] == (row-1, column) and seen[row-1][column] == (row-2,column):
        #         return False
    elif direction == "L":
        if column+2 < column_numbers:
            if seen[row][column] == (row, column+1) and seen[row][column+1] == (row, column+2):
                return False
        # if column+3 < column_numbers:
        #     if seen[row][column] == (row, column+1) and seen[row][column+1] == (row, column+2) and seen[row][column+2] == (row, column+3):
        #         return False
    elif direction == "R":
        if 0 <= column-2:
            if seen[row][column] == (row, column-1) and seen[row][column-1] == (row, column-2):
                return False
        # if 0 <= column-3:
        #     if seen[row][column] == (row, column-1) and seen[row][column-1] == (row, column-2) and seen[row][column-2] == (row, column-3):
        #         return False
    return True

with open("Day17/input-example.txt", "r") as file:
    grid = [list(map(int, line.strip())) for line in file if line.strip()]


row_numbers = len(grid)
column_numbers = len(grid[0])

min_dis = [[float('inf') for _ in range(row_numbers)] for _ in range(column_numbers)]
min_dis[0][0] = 0
seen = [[(-1,-1) for _ in range(row_numbers)] for _ in range(column_numbers)]

for time in range(10):
    # for row, column in iterate_diagonally(grid):
    for row in range(row_numbers):
        for column in range(column_numbers):
            if 0 <= row-1: 
                cur_dis = min_dis[row][column] + grid[row-1][column]
                if cur_dis < min_dis[row-1][column] and is_not_consec(row, column, "U"):
                    min_dis[row-1][column] = cur_dis
                    seen[row-1][column] = (row, column)
            if row+1 < row_numbers:
                cur_dis = min_dis[row][column] + grid[row+1][column]
                if cur_dis < min_dis[row+1][column] and is_not_consec(row, column, "D"):
                    min_dis[row+1][column] = cur_dis
                    seen[row+1][column] = (row, column)
            if 0 <= column-1: 
                cur_dis = min_dis[row][column] + grid[row][column-1]
                if cur_dis < min_dis[row][column-1] and is_not_consec(row, column, "L"):
                    min_dis[row][column-1] = cur_dis
                    seen[row][column-1] = (row, column)
            if column+1 < column_numbers: 
                cur_dis = min_dis[row][column] + grid[row][column+1]
                if cur_dis < min_dis[row][column+1] and is_not_consec(row, column, "R"):
                    min_dis[row][column+1] = cur_dis
                    seen[row][column+1] = (row, column)

# Open a file in write mode
with open('Day17\output_old.txt', 'w') as file:
    for row in seen:
        # Convert each row to a string and write it to the file
        file.write(' '.join(map(str, row)) + '\n')

#962 too high