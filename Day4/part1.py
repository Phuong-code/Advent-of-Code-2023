def get_point(card):
    win_numbers = card[card.index(":")+1:card.index("|")].split()
    number_you_have = card[card.index("|")+1:].split()
    point = 0
    for number in number_you_have:
        if number in win_numbers:
            if point == 0:
                point =1
            else:
                point *= 2
    return point

file = open("Day4\input.txt", "r")
content = file.readlines()
# print(content)
file.close()

sum = 0
for card in content:
    sum += get_point(card)
print(sum)