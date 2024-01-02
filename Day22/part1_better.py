with open("Day22\input.txt", "r") as file:
    bricks = [list(map(int, line.replace("~", ",").split(","))) for line in file.read().split("\n")]
    bricks.sort(key=lambda x: x[2])

def is_overlap(brick, check):
    return max(brick[0], check[0]) <= min(brick[3], check[3]) and max(brick[1], check[1]) <= min(brick[4], check[4])

for index, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:index]:    
        if is_overlap(brick, check):
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

k_supports_v = {i: set() for i in range(len(bricks))}
v_depends_k = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if is_overlap(upper, lower) and lower[5] + 1 == upper[2]:
            k_supports_v[i].add(j)
            v_depends_k[j].add(i)

total = 0
for i in range(len(bricks)):
    if all(len(v_depends_k[j]) >= 2 for j in k_supports_v[i]):
        total += 1

print(total)



