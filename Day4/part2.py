def get_matches(card):
    card_id = int(card[4:card.index(":")].strip())
    win_numbers = card[card.index(":")+1:card.index("|")].split()
    number_you_have = card[card.index("|")+1:].split()
    matches = 0
    for number in number_you_have:
        if number in win_numbers:
            matches +=1

    return matches

file = open("Day4\input.txt", "r")
cards = file.readlines()
# print(content)
file.close()

dp = [1] * len(cards)
for i in range(len(cards)):
    for j in range(get_matches(cards[i])):
        dp[i+j+1] += dp[i]

print(sum(dp))