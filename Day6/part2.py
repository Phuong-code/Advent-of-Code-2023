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
# print(content)
file.close()

content[0] = int(content[0][5:].replace(" ","").replace("\n",""))
content[1] = int(content[1][9:].replace(" ",""))

print(get_numbers_of_ways(content))
