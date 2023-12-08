def get_result(instructions, dict):
    destination = "AAA"
    step = 0
    while (destination != "ZZZ"):
        for instruction in instructions:
            if instruction == "L":
                destination = dict[destination][0]
            else:
                destination = dict[destination][1]
            step += 1
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

print(get_result(instructions, dict))