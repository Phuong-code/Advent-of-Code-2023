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

file = open("Day14\input.txt", "r")
content = file.read()
file.close()
block = content.split("\n")
print(get_load(block))

# 111339 correct
