dict ={"one":"o1e",
       "two":"t2o",
       "three":"t3e",
       "four":"f4r",
       "five":"f5e",
       "six":"s6x",
       "seven":"s7n",
       "eight":"e8t",
       "nine":"n9e"}

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

def convert_to_number_string(line):
    identical_line = line
    for key, val in dict.items():
        if key in line:
            identical_line = identical_line.replace(key, val)
    return identical_line

file = open("input.txt", "r")
content = file.readlines()
# print(content)
file.close()

sum = 0
for line in content:
    sum += sum_one_line(convert_to_number_string(line))
print(sum)

# print(sum_one_line(convert_to_number_string("1vvssfvlfbg2eightmxbqbvgsixnine")))





