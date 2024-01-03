with open("Day24\input.txt", "r") as file:
    stones = [list(map(int, line.replace(" @", ",").split(", "))) for line in file.read().split("\n")]

graph_dict = {}

def get_graph(stone):
    x1 = stone[0]
    y1 = stone[1]
    x2 = stone[0] + stone[3]
    y2 = stone[1] + stone[4]
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return (a, b)

for index, stone in enumerate(stones):
    graph_dict[index] = get_graph(stone)

def get_intersect(graph1, graph2):
    a1 = graph1[0]
    b1 = graph1[1]
    a2 = graph2[0]
    b2 = graph2[1]
    if a1 == a2:
        return 0
    else:
        x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return (x, y)
        
def is_future(stone1, stone2, intersect):
    for stone in [stone1, stone2]:
        for axis in range(2):  
            position = stone[axis]
            velocity = stone[axis + 3]
            intersection_point = intersect[axis]

            if velocity > 0 and intersection_point < position:
                return False

            elif velocity < 0 and intersection_point > position:
                return False
    return True
        
    
test_min = 200000000000000
test_max = 400000000000000
total = 0
for i in range(len(stones)):
    for j in range(i+1, len(stones)):
        intersect = get_intersect(graph_dict[i], graph_dict[j])
        if intersect == 0:
            continue
        else:
            if is_future(stones[i], stones[j], intersect) and test_min <= intersect[0] <= test_max and test_min <= intersect[1] <= test_max:
                total += 1

print(total)



