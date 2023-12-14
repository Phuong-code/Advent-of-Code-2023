def is_valid(spring, group):
    group_result = []
    count = 0
    for c in spring:
        if c == "#":
            count += 1
        elif count > 0:
            group_result.append(count)
            count = 0
    if count != 0:
        group_result.append(count)
    return group_result == group

def count_all_pos(spring, group):
    if "?" not in spring:
        if is_valid(spring, group):
            return 1
        else:
            return 0
    count = 0
    for i in range(len(spring)):
        if spring[i] == "?":
            count += count_all_pos(spring[:i]+"."+spring[i+1:], group)
            count += count_all_pos(spring[:i]+"#"+spring[i+1:], group)
            break
    return count

file = open("Day12\input.txt","r")
content = file.read().split("\n")
file.close()

sum = 0
for line in content:
    spring, group = line.split()
    group = list(map(int, group.split(",")))
    sum += count_all_pos(spring, group)

print(sum)


