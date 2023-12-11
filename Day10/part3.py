file = open('Day10\output.txt','r')
content = file.read().split("\n")
file.close()

grid =[[0 for _ in range(len(content[0]))] for _ in range(len(content))]
for row in range(len(content)):
    for column in range(len(content[0])):
        grid[row][column] = content[row][column]

for row in range(1, len(grid)):
    for column in range(1, len(grid[0])):
        if grid[row-1][column] == "O" and grid[row][column-1] == "O":
            grid[row][column] = "O"
            break


result = 0
for row in range(len(grid)):
    for column in range(len(grid[0])):
        if grid[row][column] == "O":
            result += 1
print(result)