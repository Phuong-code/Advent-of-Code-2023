def hashe(step):
    value = 0
    for char in step:
        value = ((value + ord(char)) * 17) % 256
    return value


file = open("Day15\input.txt","r")
content = file.read()
file.close()

steps = content.split(",")
boxes = [[] for _ in range(256)]

for step in steps:
    if "=" in step:
        box = boxes[hashe(step[0:-2])]
        new_len = True
        for i in range(len(box)):
            if step[0:-2] == box[i][0:-2]:
                box[i] = step.replace("="," ")
                new_len = False
                break
        if new_len:
            box.append(step.replace("="," "))
    elif "-" in step:
        box = boxes[hashe(step[0:-1])]
        for lens in box:
            if step[0:-1] == lens[0:-2]:
                box.remove(lens)

result = 0
for i in range(len(boxes)):
    if len(boxes[i]) != 0:
        for j in range(len(boxes[i])):
            result += (i+1) * (j+1) * int(boxes[i][j][-1])
print(result)





