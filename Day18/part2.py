HEX_DIRECTION_MAP  = {"0":"R",
                    "1":"D",
                    "2":"L",
                    "3":"U"}

def convert_to_instruction(instruction):
    direction = HEX_DIRECTION_MAP[instruction[-1]]
    meter = int(instruction[0:-1], 16)
    return (direction, meter)

with open("Day18\input.txt", "r") as file:
    instructions = [line[line.index("#")+1:-1] for line in file.read().split("\n")]

for i in range(len(instructions)):
    instructions[i] = convert_to_instruction(instructions[i])

points = [(0, 0)]

dirs = {"R" : (0, 1),
        "D" : (1, 0),
        "L" : (0, -1),
        "U" : (-1, 0)}

cur_point = points[0]
b = 0
for ins in instructions:
    dir = ins[0]
    meter = ins[1]
    b += meter
    cur_point = (cur_point[0] + dirs[dir][0] * meter, cur_point[1] + dirs[dir][1] * meter)
    points.append(cur_point)

A = 0
for i in range(len(points)-1):
    A += (points[i][1] + points[i+1][1]) * (points[i][0] - points[i+1][0])
A = abs(A//2)

i = A - b//2 +1 + b
print(i)