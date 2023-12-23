def hashe(step):
    value = 0
    for char in step:
        value = ((value + ord(char)) * 17) % 256
    return value


file = open("Day15\input.txt","r")
content = file.read()
file.close()

steps = content.split(",")

result = 0
for step in steps:
    result += hashe(step)

print(result)