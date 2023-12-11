file = open('Day11\input.txt','r')
content = file.read().split("\n")
file.close()

grid =[[0 for _ in range(len(content[0]))] for _ in range(len(content))]
for row in range(len(content)):
    for column in range(len(content[0])):
        grid[row][column] = content[row][column]

empty_row =[]
for row in range(len(grid[0])):
    all_same = True
    for element in grid[row][1:]:
        if element != grid[row][0]:
            all_same = False
            break
    if all_same == True:
        empty_row.append(row)

rows, cols = len(grid), len(grid[0])
transposed_grid = [[grid[j][i] for j in range(rows)] for i in range(cols)]

empty_column = []
for row in range(len(transposed_grid)):
    all_same = True
    for element in transposed_grid[row][1:]:
        if element != transposed_grid[row][0]:
            all_same = False
            break
    if all_same == True:
        empty_column.append(row)

# print(empty_row)
# print(empty_column)

def get_distance(a ,b, expand):
    x = abs(b[0] - a[0])
    columns = 0
    for number in empty_column:
        if min(a[1], b[1]) < number < max(a[1], b[1]):
            columns += 1

    y = abs(b[1] - a[1])
    rows = 0
    for number in empty_row:
        if min(a[0], b[0]) < number < max(a[0], b[0]):
            rows += 1

    result = x + y + (columns+rows)*(expand-1)
    return result

star_location = []
for row in range(len(grid)):
    for column in range(len(grid[0])):
        if grid[row][column] == "#":
            star_location.append([row, column])

sum = 0
expand = 1000000
# expand = 99
# print(star_location)
for i in range(len(star_location)):
    for j in range(i+1,len(star_location)):
        sum += get_distance(star_location[i], star_location[j], expand)
print(sum)

# 82000210 too low