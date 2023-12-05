def convert_seed(seeds, map):
    converted_seeds = []
    for line in map:
        list = line.split()
        list[0] = int(list[0])
        list[1] = int(list[1])
        list[2] = int(list[2])
        diff = list[1]-list[0]
        for i in range(len(seeds)): 
            if seeds[i] != "":
                if (list[1] <= seeds[i]) and (seeds[i] <= (list[1] + list[2] -1)):
                    seeds[i] -= diff
                    converted_seeds.append(seeds[i])
                    seeds[i] = ""
    for seed in seeds:
        if seed != "":
            converted_seeds.append(seed)
    return converted_seeds


file = open("Day5\input.txt", "r")
content = file.readlines()
# print(content)
file.close()

seeds = content[0][content[0].index(":")+1:].split()
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])
# print(seeds)

# seeds = [81, 53, 57, 52]

seed_to_soild_map = content[content.index("seed-to-soil map:\n")+1:content.index("soil-to-fertilizer map:\n")-1]
soil_to_fertilizier_map = content[content.index("soil-to-fertilizer map:\n")+1:content.index("fertilizer-to-water map:\n")-1]
fertilizer_to_water_map = content[content.index("fertilizer-to-water map:\n")+1:content.index("water-to-light map:\n")-1]
water_to_light_map = content[content.index("water-to-light map:\n")+1:content.index("light-to-temperature map:\n")-1]
light_to_temperature_map = content[content.index("light-to-temperature map:\n")+1:content.index("temperature-to-humidity map:\n")-1]
temperature_to_humidity_map = content[content.index("temperature-to-humidity map:\n")+1:content.index("humidity-to-location map:\n")-1]
humidity_to_location_map = content[content.index("humidity-to-location map:\n")+1:]

# convert_seed(seeds, seed_to_soild_map)
seeds = convert_seed(seeds, seed_to_soild_map)
seeds = convert_seed(seeds,soil_to_fertilizier_map)
seeds = convert_seed(seeds, fertilizer_to_water_map)
seeds = convert_seed(seeds, water_to_light_map)
seeds = convert_seed(seeds, light_to_temperature_map)
seeds = convert_seed(seeds, temperature_to_humidity_map)
seeds = convert_seed(seeds,humidity_to_location_map)

print("min:")
print(min(seeds))