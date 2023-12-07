def get_type(cards):
    duplicate_dict ={}
    for card in cards:
        if card not in duplicate_dict:
            duplicate_dict[card] = 1
        else:
            duplicate_dict[card] += 1
    for key, val in duplicate_dict.items():
        if val == 5:
            return 6 # five of a kind
        if val == 4:
            return 5 # four of a kind
        if val == 3:
            for val2 in duplicate_dict.values():
                if val2 == 2:
                    return 4 # full house
            return 3 # three of a kind
        if val == 2:
            for key2, val2 in duplicate_dict.items():
                if val2 == 3:
                    return 4 # full house
                elif val2 == 2 and key != key2:
                    return 2 # two pair
            return 1 # one pair
    return 0 # high card

def convert_joker(cards):
    if "J" in cards:
        duplicate_dict = {}
        new_cards = ""
        for card in cards:
            if card != "J":
                if card not in duplicate_dict:
                    duplicate_dict[card] = 1
                else:
                    duplicate_dict[card] += 1
        if len(duplicate_dict) == 0:
            return cards
        key = max(duplicate_dict, key=duplicate_dict.get)
        for card in cards:
            if card == "J":
                new_cards += key
            else:
                new_cards += card
        return new_cards
    return cards

print(convert_joker("QQQJA"))
        
dict = {"J":"a",
        "2":"b",
        "3":"c",
        "4":"d",
        "5":"e",
        "6":"f",
        "7":"g",
        "8":"h",
        "9":"i",
        "T":"j",
        "Q":"k",
        "K":"l",
        "A":"m"}

def convert_to_new_card(cards):
    new_card = ""
    new_card += str(get_type(convert_joker(cards)))
    for card in cards:
        if card in dict:
            new_card += dict[card]
    return new_card


file = open('Day7\input.txt','r')
content = file.readlines()
file.close()

cards_list = []
for cards in content:
    cards_list.append(cards.split())

for card in cards_list:
    card[0] = convert_to_new_card(card[0])


cards_list.sort()

sum = 0
for i in range(len(cards_list)):
    sum += (i+1) * int(cards_list[i][1])

print(sum)
