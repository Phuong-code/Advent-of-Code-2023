def sum_one_line(line):
    result = 0
    number_string = ""
    for char in line:
        if char.isdigit():
            number_string += char
    if len(number_string) == 0:
        result = 0
    elif len(number_string) == 1:
        result = int(number_string+number_string)
    else:
        result = int(number_string[0] + number_string[-1])
    return result

file = open("input.txt", "r")
content = file.readlines()
# print(content)
file.close()

sum = 0
for line in content:
    sum += sum_one_line(line)

print(sum)





