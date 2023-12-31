file = open("Day12\input.txt","r")
content = file.read().split("\n")
file.close()

cache = {}

def count(spring, group):
    if spring == "":
        return 1 if group == () else 0
    
    if group == ():
        return 1 if "#" not in spring else 0

    result = 0

    key = (spring, group)
    if key in cache:
        return cache[key]

    if spring[0] in ".?":
        result += count(spring[1:], group)

    if spring[0] in "#?":
        if len(spring) >= group[0] and "." not in spring[1:group[0]] and (len(spring) == group[0] or spring[group[0]] != "#"):
            result += count(spring[group[0]+1:], group[1:])
    
    cache[key] = result
    return result


total = 0
for line in content:
    spring, group = line.split()
    group = tuple(map(int, group.split(",")))
    spring = "?".join([spring]*5)
    group = group * 5
    total += count(spring, group)

print(total)



