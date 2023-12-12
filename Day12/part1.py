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


def count_valid_arrangements(springs, group_sizes, start=0):
    """
    Recursively count the number of valid arrangements for a given row.
    """
    if '?' not in springs:
        return 1 if is_valid(springs, group_sizes) else 0

    count = 0
    for i in range(start, len(springs)):
        if springs[i] == '?':
            # Try with operational spring
            count += count_valid_arrangements(springs[:i] + '.' + springs[i+1:], group_sizes, i + 1)
            # Try with damaged spring
            count += count_valid_arrangements(springs[:i] + '#' + springs[i+1:], group_sizes, i + 1)
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


