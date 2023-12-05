def convert_to_dict(map):
    dict = {}
    for line in map:
        list = line.split()
        # list[0] = val, list[1] = key, list[3] = range
        for i in range(0, int(list[2])):
            dict[int(list[1]) + i] = int(list[0]) + i
    return dict


file = open("Day5\input.txt", "r")
content = file.readlines()
# print(content)
file.close()

seeds = content[0][content[0].index(":")+1:].split()
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])
# print(seeds)

seed_to_soild_map = content[content.index("seed-to-soil map:\n")+1:content.index("soil-to-fertilizer map:\n")-1]
soil_to_fertilizier_map = content[content.index("soil-to-fertilizer map:\n")+1:content.index("fertilizer-to-water map:\n")-1]
fertilizer_to_water_map = content[content.index("fertilizer-to-water map:\n")+1:content.index("water-to-light map:\n")-1]
water_to_light_map = content[content.index("water-to-light map:\n")+1:content.index("light-to-temperature map:\n")-1]
light_to_temperature_map = content[content.index("light-to-temperature map:\n")+1:content.index("temperature-to-humidity map:\n")-1]
temperature_to_humidity_map = content[content.index("temperature-to-humidity map:\n")+1:content.index("humidity-to-location map:\n")-1]
humidity_to_location_map = content[content.index("humidity-to-location map:\n")+1:]

# print(seed_to_soild_map)
# print(soil_to_fertilizier_map)
# print(fertilizer_to_water_map)
# print(water_to_light_map)
# print(light_to_temperature_map)
# print(temperature_to_humidity_map)
# print(humidity_to_location_map)

# print(convert_to_dict(seed_to_soild_map))

dict1 = convert_to_dict(seed_to_soild_map)
# print(dict1)
dict2 = convert_to_dict(soil_to_fertilizier_map)
dict3 = convert_to_dict(fertilizer_to_water_map)
dict4 = convert_to_dict(water_to_light_map)
dict5 = convert_to_dict(light_to_temperature_map)
dict6 = convert_to_dict(temperature_to_humidity_map)
dict7 = convert_to_dict(humidity_to_location_map)

for i in range(len(seeds)):
    # print(seeds[i])
    if seeds[i] in dict1:
        seeds[i] = dict1[seeds[i]]
# print(seeds)

for i in range(len(seeds)):
    if seeds[i] in dict2:
        seeds[i] = dict2[seeds[i]]

# print(seeds)
for i in range(len(seeds)):
    if seeds[i] in dict3:
        seeds[i] = dict3[seeds[i]]
for i in range(len(seeds)):
    if seeds[i] in dict4:
        seeds[i] = dict4[seeds[i]]
for i in range(len(seeds)):
    if seeds[i] in dict5:
        seeds[i] = dict5[seeds[i]]
for i in range(len(seeds)):
    if seeds[i] in dict6:
        seeds[i] = dict6[seeds[i]]
for i in range(len(seeds)):
    if seeds[i] in dict7:
        seeds[i] = dict7[seeds[i]]

print("min:")
print(min(seeds))