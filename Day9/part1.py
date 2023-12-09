file = open('Day9\input.txt','r')
content = file.read().split("\n")
file.close()

input_list = []
for string in content:
    input_list.append(list(map(int, string.split())))

def get_next_value(list):
    result = list[-1]
    sublist = []
    for i in range(0,len(list)-1):
        sublist.append(list[i+1]-list[i])
    if sum(sublist) == 0 and sublist != []:
        return result
    return result + get_next_value(sublist)

total_sum = 0
for list in input_list:
    total_sum += get_next_value(list)
print(total_sum)