with open("Day22\input.txt", "r") as file:
    blocks = [tuple(line.split("~")) for line in file.read().split("\n")]
    blocks = [(tuple(map(int, block[0].split(","))), tuple(map(int, block[1].split(",")))) for block in blocks]
    blocks = sorted(blocks, key=lambda x: x[0][2])

x_num = 10
y_num = 10
z_num = 302
grid = [[[0 for _ in range(z_num)] for _ in range(y_num)] for _ in range(x_num)]

for i in range(len(blocks)):
    j = 0
    s = 0
    e = 0
    while j < 3:
        if blocks[i][0][j] != blocks[i][1][j]:
            s = blocks[i][0][j]
            e = blocks[i][1][j]
            break
        j += 1
    x = blocks[i][0][0]
    y = blocks[i][0][1]
    z = blocks[i][0][2]
    for k in range(s, e+1):
        if j == 0:
            grid[k][y][z] = i+1
        elif j == 1:
            grid[x][k][z] = i+1
        elif j == 2:
            grid[x][y][k] = i+1
        elif j == 3:
            grid[x][y][z] = i+1
            break

def fall(grid):
    for block_num in range(1, len(blocks)+1):
        block_list = []
        for x in range(x_num):
            for y in range(y_num):
                for z in range(z_num):
                    if grid[x][y][z] == block_num:
                        block_list.append((x, y, z))
        if len(block_list) != 0:
            if all(b[2] == block_list[0][2] for b in block_list):
                while block_list[0][2] != 1:
                    valid_block = []
                    for block in block_list:
                        x1 = block[0]
                        y1 = block[1]
                        z1 = block[2]
                        if grid[x1][y1][z1-1] == 0:
                            valid_block.append(True)
                        else:
                            valid_block.append(False)
                    if all(valid_block):
                        copy_block_list = []
                        for block in block_list:
                            x1 = block[0]
                            y1 = block[1]
                            z1 = block[2]
                            grid[x1][y1][z1-1] = block_num
                            grid[x1][y1][z1] = 0
                            copy_block_list.append((x1, y1, z1-1))
                        block_list = copy_block_list
                    else:
                        break
            else:
                block_list = sorted(block_list, key=lambda x: x[2])
                while block_list[0][2] != 1:
                    x1_first = block_list[0][0]
                    y1_first = block_list[0][1]
                    z1_first = block_list[0][2]
                    x1_last = block_list[-1][0]
                    y1_last = block_list[-1][1]
                    z1_last = block_list[-1][2]
                    if grid[x1_first][y1_first][z1_first-1] == 0:
                        grid[x1_first][y1_first][z1_first-1] = block_num
                        grid[x1_last][y1_last][z1_last] = 0
                        block_list.insert(0, (x1_first, y1_first, z1_first-1))
                        block_list.pop()
                    else:
                        break


def can_fall(grid, start_block_list):
    up_block_list = []
    if all(b[2] == start_block_list[0][2] for b in start_block_list):
        for x in range(x_num):
            for y in range(y_num):
                up_block_num = grid[x][y][start_block_list[0][2]+1] 
                if up_block_num != 0:
                    up_block_list.append(up_block_num)
    else:
        start_block_list = sorted(start_block_list, key=lambda x: x[2])
        for x in range(x_num):
            for y in range(y_num):
                up_block_num = grid[x][y][start_block_list[-1][2]+1] 
                if up_block_num != 0:
                    up_block_list.append(up_block_num)  
    
    if len(up_block_list) == 0:
        return False
    else:
        for block_num in up_block_list:
            block_list = []
            for x in range(x_num):
                for y in range(y_num):
                    for z in range(z_num):
                        if grid[x][y][z] == block_num:
                            block_list.append((x, y, z))
            if len(block_list) != 0:
                if all(b[2] == block_list[0][2] for b in block_list):
                    if block_list[0][2] != 1:
                        valid_block = []
                        for block in block_list:
                            x1 = block[0]
                            y1 = block[1]
                            z1 = block[2]
                            if grid[x1][y1][z1-1] == 0:
                                valid_block.append(True)
                            else:
                                valid_block.append(False)
                        if all(valid_block):
                            return True
                else:
                    block_list = sorted(block_list, key=lambda x: x[2])
                    if block_list[0][2] != 1:
                        x1_first = block_list[0][0]
                        y1_first = block_list[0][1]
                        z1_first = block_list[0][2]
                        if grid[x1_first][y1_first][z1_first-1] == 0:
                            return True
    return False

fall(grid)

total = 0
for block_num in range(1, len(blocks)+1):
    block_list = []
    for x in range(x_num):
        for y in range(y_num):
            for z in range(z_num):
                if grid[x][y][z] == block_num:
                    grid[x][y][z] = 0
                    block_list.append((x, y, z))   
    if not can_fall(grid, block_list):
        total += 1
        print("computing:...", total)
    for block in block_list:
        grid[block[0]][block[1]][block[2]] = block_num

print("final:",total)

# 441 correct
