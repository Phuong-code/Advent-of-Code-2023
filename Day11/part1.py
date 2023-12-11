file = open('Day11\input.txt','r')
content = file.read().split("\n")
file.close()

grid =[[0 for _ in range(len(content[0]))] for _ in range(len(content))]
for row in range(len(content)):
    for column in range(len(content[0])):
        grid[row][column] = content[row][column]

grid2 =[]
new_row = ["."]*len(grid[0])
for row in range(len(grid[0])):
    all_same = True
    for element in grid[row][1:]:
        if element != grid[row][0]:
            all_same = False
            break
    if all_same == True:
        grid2.append(new_row)
    grid2.append(grid[row])

rows, cols = len(grid2), len(grid2[0])
transposed_grid2 = [[grid2[j][i] for j in range(rows)] for i in range(cols)]

grid3 = []
new_row = ["."]*len(transposed_grid2[0])
for row in range(len(transposed_grid2)):
    all_same = True
    for element in transposed_grid2[row][1:]:
        if element != transposed_grid2[row][0]:
            all_same = False
            break
    if all_same == True:
        grid3.append(new_row)
    grid3.append(transposed_grid2[row])

rows, cols = len(grid3), len(grid3[0])
transposed_grid3 = [[grid3[j][i] for j in range(rows)] for i in range(cols)]

grid = transposed_grid3
# with open('Day11\output.txt', 'w') as file:
#     for row_idx, row in enumerate(grid):
#         file.write(' '.join(map(str, row)) + '\n')

def get_distance(a ,b):
    x = abs(b[0] - a[0])
    y = abs(b[1] - a[1])
    return x+y

star_location = []
for row in range(len(grid)):
    for column in range(len(grid[0])):
        if grid[row][column] == "#":
            star_location.append([row, column])

sum = 0
for i in range(len(star_location)):
    for j in range(i+1,len(star_location)):
        sum += get_distance(star_location[i], star_location[j])
print(sum)