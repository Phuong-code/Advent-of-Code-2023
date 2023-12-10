'''
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''

dict = {
    "N":["|", "7", "F"],
    "W":["-", "L", "F"],
    "E":["-", "J", "7"],
    "S":["|", "L", "J"],
}

dict2 = {
    "|":["N", "S"],
    "-":["E", "W"],
    "L":["N", "E"],
    "J":["N", "W"],
    "7":["W", "S"],
    "F":["S", "E"]
}

def is_connected(start, end, end_position):
    if start == "." or end == ".":
        return False
    elif end == "S":
        return True
    else:
        if end in dict[end_position]:
            return True



def check_around(grid, row, column, step, pre_row, pre_column):
    for dicrection in dict2[grid[row][column]]:
        if dicrection == "N":
            if pre_row != row-1 or pre_column != column:
                if grid[row-1][column] == "S":
                    step += 1
                    return step
                if is_connected(grid[row][column], grid[row-1][column], dicrection): #top 
                    step += 1
                    return check_around(grid, row-1, column, step, row, column)
        if dicrection == "W":
            if pre_row != row or pre_column != column-1:
                if grid[row][column-1] == "S":
                    step += 1
                    return step
                if is_connected(grid[row][column], grid[row][column-1], dicrection): #left
                    step += 1
                    return check_around(grid, row, column-1, step, row, column)
        if dicrection == "E":
            if pre_row != row or pre_column != column+1:
                if grid[row][column+1] == "S":
                    step += 1
                    return step
                if is_connected(grid[row][column], grid[row][column+1], dicrection): #right
                    step += 1
                    return check_around(grid, row, column+1, step, row, column)
        if dicrection == "S":
            if pre_row != row+1 or pre_column != column:
                if grid[row+1][column] == "S":
                    step += 1
                    return step
                if is_connected(grid[row][column], grid[row+1][column], dicrection): #bottom
                    step += 1
                    return check_around(grid, row+1, column, step, row, column)
    
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

step = 1
# print(grid[s_row][s_column-1])
# print(check_around(grid, s_row, s_column-1, step, s_row, s_column)//2)
# print(check_around(grid, s_row, s_column+1, step, s_row, s_column)//2)
# print(check_around(grid, s_row-1, s_column, step, s_row, s_column)//2)
print(check_around(grid, s_row+1, s_column, step, s_row, s_column)//2)




