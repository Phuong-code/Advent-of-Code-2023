def get_result(instructions, dict, start):
    destination = start
    step = 0
    while (destination[-1] != "Z"):
        for instruction in instructions:
            if instruction == "L":
                destination = dict[destination][0]
            elif instruction == "R":
                destination = dict[destination][1]
            step += 1
            if destination[-1] == "Z":
                return step
    return step

file = open('Day8\input.txt','r')
content = file.read().split("\n")
file.close()

instructions = content[0]
map = content[2:]

dict = {}
for line in map:
    start = line[:3]
    left = line[line.index("(")+1:line.index(",")].strip()
    right = line[line.index(",")+1:line.index(")")].strip()
    if start not in dict:
        dict[start] = [left, right]


result_list = []
for key, val in dict.items():
    if key[-1] == "A":
        result = get_result(instructions, dict, key)
        result_list.append(result)

import math
from functools import reduce
result = reduce(math.lcm, result_list)

print(result)