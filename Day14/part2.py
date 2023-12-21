def get_load(block):
    sum = 0
    num_columns = len(block[0])
    for column in range(num_columns):
        base = 0
        for row in range(len(block)):
            if block[row][column] == "O":
                sum += num_columns - base
                base += 1
            elif block[row][column] == "#":
                base = row + 1
            else:
                continue
    return sum

def tilt_north():
    global block
    new_block = []
    num_columns = len(block[0])
    for column in range(num_columns):
        new_row = ""
        for row in range(len(block)):
            new_row += block[row][column]
        new_block.append(new_row)
    block = new_block

    new_block = []
    for row in range(len(block)):
        row_list = block[row].split("#")
        new_row = ""
        new_row_list = []
        for group in row_list:
            sorted_string = ''.join(sorted(group, reverse=True))
            new_row_list.append(sorted_string)
            new_row = "#".join(new_row_list)
        new_block.append(new_row)
    block = new_block

    new_block = []
    for column in range(len(block[0])):
        new_row = ""
        for row in range(len(block)):
            new_row += block[row][column]
        new_block.append(new_row)
    block = new_block

def rotate():
    global block
    new_block = []
    for column in range(len(block[0])):
        new_row = ""
        for row in range(len(block)-1,-1,-1):
            new_row += block[row][column]
        new_block.append(new_row)
    block = new_block
    

file = open("Day14\input.txt", "r")
content = file.read()
file.close()
block = content.split("\n")


seen = {tuple(block)}
array = [tuple(block)]
while True:
    for _ in range(4):
        tilt_north()
        rotate()
    if tuple(block) in seen:
        break
    seen.add(tuple(block))
    array.append(tuple(block))
first = array.index(tuple(block))
block = array[(1000000000 - first) % (len(array) - first) + first]

print(sum(row.count("O") * (len(block) - r) for r, row in enumerate(block)))

# 93736 correct