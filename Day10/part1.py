dict = {
    "|":["N", "S"],
    "-":["E", "W"],
    "L":["N", "E"],
    "J":["N", "W"],
    "7":["W", "S"],
    "F":["S", "E"]
}

def count_step(grid, row, column, dicrection):
    step = 0
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
        step += 1
        next = grid[row][column]
        if next == "S":
            step += 1
            return step
        for val in dict[next]:
            if val != dicrection:
                dicrection = val
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

print(count_step(grid, s_row-1, s_column, "E")//2) #input
# print(count_step(grid, s_row, s_column+1, "E")) #example
# print(count_step(grid, s_row, s_column+1, "N")) #example 2
