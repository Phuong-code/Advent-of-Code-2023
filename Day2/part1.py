# only 12 red cubes, 13 green cubes, and 14 blue cubes

dict = {
    "red":12,
    "green":13,
    "blue":14
}

def get_number_of_cubes(cubes):
    cubes = cubes.strip().split(" ")
    return int(cubes[0])



def check_subdraw(draw):
    draw_list = draw.split(",")
    for cubes in draw_list:
        for key, val in dict.items():
            if key in cubes:
                if get_number_of_cubes(cubes) > dict[key]:
                    return False
    return True

def check_game(game):
    game_id = int(game[5:game.index(":")])
    game_list = game[game.index(":")+1:].split(";")
    for draw in game_list:
        if check_subdraw(draw) == False:
            return 0
    return game_id

file = open("input.txt", "r")
content = file.readlines()
# print(content)
file.close()

sum = 0
for line in content:
    sum += check_game(line)

print(sum)