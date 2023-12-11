dict = {
    "|":["N", "S"],
    "-":["E", "W"],
    "L":["N", "E"],
    "J":["N", "W"],
    "7":["W", "S"],
    "F":["S", "E"]
}

def get_map_index(grid, row, column, dicrection, map_index):
    # step = 0
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
        # step += 1
        next = grid[row][column]
        if next == "S":
            # step += 1
            map_index.append([row, column])
            return map_index
        for val in dict[next]:
            if val != dicrection:
                dicrection = val
                map_index.append([row, column])
                break

def get_tile_right(grid, row, column, dicrection, map_index):
    tile_index = []
    tile = 0
    while grid[row][column] != "S":
        if dicrection == "N":
            right = [row, column+1]
            if right not in map_index and right not in tile_index:
                tile_index.append(right)
                tile += 1
            if grid[row][column] == "J":
                back = [row+1, column]
                if back not in map_index and back not in tile_index:
                    tile_index.append(back)
                    tile += 1
            row -= 1
            dicrection = "S"
        elif dicrection == "W":
            right = [row-1, column]
            if right not in map_index and right not in tile_index:
                tile_index.append(right)
                tile += 1
            if grid[row][column] == "7":
                back = [row, column+1]
                if back not in map_index and back not in tile_index:
                    tile_index.append(back)
                    tile += 1
            column -= 1
            dicrection = "E"
        elif dicrection == "S":
            right = [row, column-1]
            if right not in map_index and right not in tile_index:
                tile_index.append(right)
                tile += 1
            if grid[row][column] == "F":
                back = [row-1, column]  
                if back not in map_index and back not in tile_index:
                    tile_index.append(back)
                    tile += 1
            row += 1
            dicrection = "N"
        elif dicrection == "E":
            right = [row+1, column]
            if right not in map_index and right not in tile_index:
                tile_index.append(right)
                tile += 1
            if grid[row][column] == "L":
                back = [row, column-1]  
                if back not in map_index and back not in tile_index:
                    tile_index.append(back)
                    tile += 1
            column += 1
            dicrection = "W"
        next = grid[row][column]
        if next == "S":
            return tile_index
        for val in dict[next]:
            if val != dicrection:
                dicrection = val
                break

def get_tile_left(grid, row, column, dicrection, map_index):
    tile_index = []
    tile = 0
    while grid[row][column] != "S":
        if dicrection == "N":
            left = [row, column-1]
            if left not in map_index and left not in tile_index:
                tile_index.append(left)
                tile += 1
            if grid[row][column] == "L":
                back = [row+1, column]
                if back not in map_index and back not in tile_index:
                    tile_index.append(back)
                    tile += 1
            row -= 1
            dicrection = "S"
        elif dicrection == "W":
            left = [row+1, column]
            if left not in map_index and left not in tile_index:
                tile_index.append(left)
                tile += 1
            if grid[row][column] == "J":
                back = [row, column+1]
                if back not in map_index and back not in tile_index:
                    tile_index.append(back)
                    tile += 1
            column -= 1
            dicrection = "E"
        elif dicrection == "S":
            left = [row, column+1]
            if left not in map_index and left not in tile_index:
                tile_index.append(left)
                tile += 1
            if grid[row][column] == "7":
                back = [row-1, column]  
                if back not in map_index and back not in tile_index:
                    tile_index.append(back)
                    tile += 1
            row += 1
            dicrection = "N"
        elif dicrection == "E":
            left = [row-1, column]
            if left not in map_index and left not in tile_index:
                tile_index.append(left)
                tile += 1
            if grid[row][column] == "F":
                back = [row, column-1]  
                if back not in map_index and back not in tile_index:
                    tile_index.append(back)
                    tile += 1
            column += 1
            dicrection = "W"
        next = grid[row][column]
        if next == "S":
            return tile
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

# map_index = [[1,2]] #input-example3
# # print(count_step(grid, s_row-1, s_column, "E")//2) #input
# map_index = get_map_index(grid, s_row, s_column+1, "E", map_index)  #input example 3
map_index = [[s_row+1,s_column]]
map_index = get_map_index(grid, s_row+1, s_column, "S", map_index)  #input example 3
# print(map_index)

# with open('Day10\map-index.txt', 'w') as file:
#     file.write(str(map_index))

tile_index = get_tile_right(grid, s_row+1, s_column, "S", map_index)

# print(len(get_tile_right(grid, s_row+1, s_column, "S", map_index)))

#381 correct answer

# Function to replace elements in grid based on map_index
def replace_and_write_grid(grid, map_index, tile_index):
    with open('Day10\output.txt', 'w') as file:
        for row_idx, row in enumerate(grid):
            for col_idx, _ in enumerate(row):
                if [row_idx, col_idx] in map_index:
                    row[col_idx] = 'X'
                if [row_idx, col_idx] in tile_index:
                    row[col_idx] = 'O'
            file.write(' '.join(map(str, row)) + '\n')

# Call the function
replace_and_write_grid(grid, map_index, tile_index)