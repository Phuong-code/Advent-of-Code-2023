def check_column(block):
    if len(block[0]) % 2 == 1:
        mid = len(block[0])//2
    else:
        mid = len(block[0])//2 - 0.5
    for column in range(0, len(block[0])-1):
        for row in range(len(block)):
            if block[row][column] != block[row][column+1]:
                break
        else:
            if column < mid:
                for row in range(len(block)):
                    if block[row][0] != block[row][column*2]:
                        break
                else:
                    return column+1
            else:
                for row in range(len(block)):
                    if block[row][len(block[0])-1] != block[row][len(block[0])-1 - mid*2+1]:
                        break
                else:
                    return column+1
    return 0

def check_row(block):
    rows, cols = len(block), len(block[0])
    block = [[block[j][i] for j in range(rows)] for i in range(cols)]
    if len(block[0]) % 2 == 1:
        mid = len(block[0])//2
    else:
        mid = len(block[0])//2 - 0.5
    for column in range(0, len(block[0])-1):
        for row in range(len(block)):
            if block[row][column] != block[row][column+1]:
                break
        else:
            if column < mid:
                for row in range(len(block)):
                    if block[row][0] != block[row][column*2]:
                        break
                else:
                    return column+1
            else:
                for row in range(len(block)):
                    if block[row][len(block[0])-1] != block[row][len(block[0])-1 - mid*2+1]:
                        break
                else:
                    return column+1
    return 0


file = open("Day13\input.txt", "r")
content = file.read()
file.close()
blocks = content.split("\n\n")

sum = 0
for i in blocks:
    block = i.split("\n")
    sum += check_column(block) + check_row(block)*100
print(sum)


