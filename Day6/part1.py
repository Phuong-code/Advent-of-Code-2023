def get_numbers_of_ways(list):
    time = list[0]
    distance = list[1]
    mid = time // 2
    for i in range(1, mid+1):
        if (i * (time-i)) > distance:
            result = (mid-i+1)*2
            if time % 2 == 1:
                return result
            else:
                return result-1

file = open("Day6\input.txt", "r")
content = file.readlines()
print(content)
file.close()

list1 = content[0].split()
list2 = content[1].split()
new = []
for i in range(1, len(list1)):
    new.append([int(list1[i]), int(list2[i])])

power = 1
for i in new:
    power *= get_numbers_of_ways(i)
print(power)

