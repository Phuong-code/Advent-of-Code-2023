def get_number_of_cubes(cubes):  # "4 cubes" --> 4
    cubes = cubes.strip().split(" ")
    return int(cubes[0])


def get_fewest_cubes_in_game(game): 
    dict = {
    "red":0,
    "green":0,
    "blue":0
}
    game_list = game[game.index(":")+1:].split(";")
    for game in game_list:
#  "4 red, 5 blue, 9 green" --> ["4 red", "5 blue", "9 green"]
        draw_list = game.split(",")
        for cubes in draw_list:
            for key, val in dict.items():
                if key in cubes:
                    if get_number_of_cubes(cubes) > dict[key]:
                        dict[key] = get_number_of_cubes(cubes)
    return dict

def get_power(game):
    power = 1
    # game_id = int(game[5:game.index(":")])
    fewest_cubes_dict = get_fewest_cubes_in_game(game)
    for val in fewest_cubes_dict.values():
        power*= val
    return power

file = open("input.txt", "r")
content = file.readlines()
# print(content)
file.close()

sum = 0
for line in content:
    sum += get_power(line)

print(sum)